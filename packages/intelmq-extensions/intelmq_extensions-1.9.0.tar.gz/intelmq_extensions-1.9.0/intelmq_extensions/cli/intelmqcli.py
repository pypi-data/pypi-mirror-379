#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" """

import csv
import datetime
import io
import locale
import os
import readline  # noqa: F401 hooks into input()
import subprocess
import sys
import tempfile
import zipfile
from functools import lru_cache
from time import sleep

import tabulate
from termstyle import bold, inverted, reset

from intelmq_extensions.cli import lib

myinverted = str(reset) + str(inverted)


class IntelMQCLIContoller(lib.IntelMQCLIContollerTemplate):
    appname = "intelmqcli"
    usage = lib.USAGE
    epilog = lib.EPILOG
    table_mode = False  # for sticky table mode
    dryrun = False
    verbose = False
    batch = False
    compress_csv = False
    boilerplate = None
    zipme = False
    subject = None

    def __init__(self, overridden_config: dict = None):
        super().__init__(overridden_config)
        self._collected_descriptions = set()

    def run(self, args: list):
        self.parser.add_argument(
            "-l", "--list-feeds", action="store_true", help="List all feeds"
        )
        self.parser.add_argument(
            "-i", "--list-identifiers", action="store_true", help="List all identifiers"
        )
        self.parser.add_argument(
            "-L", "--list-texts", action="store_true", help="List all existing texts."
        )
        self.parser.add_argument(
            "-t", "--text", nargs=1, help="Specify the text to be used."
        )
        self.parser.add_argument(
            "-s",
            "--subject",
            nargs=1,
            help="Specify the subject to be used instead of the per-taxonomy.",
        )
        self.parser.add_argument(
            "-T", "--list-taxonomies", action="store_true", help="List all taxonomies"
        )
        self.parser.add_argument(
            "-y", "--list-types", action="store_true", help="List all types"
        )

        self.parser.add_argument(
            "-c",
            "--compress-csv",
            action="store_true",
            help="Automatically compress/shrink the attached CSV report if"
            " fields are empty (default = False).",
        )
        self.parser.add_argument(
            "-z",
            "--zip",
            action="store_true",
            help="Zip every events.csv attachement to an "
            "investigation for RT (defaults to false)",
        )
        self.setup(args)

        if self.args.compress_csv:
            self.compress_csv = True
        if self.args.text:
            self.boilerplate = self.args.text[0]
        if self.args.zip:
            self.zipme = True
        if self.args.subject:
            self.subject = self.args.subject[0]

        self.connect_database()

        if self.args.list_feeds:
            self.execute(lib.QUERY_FEED_NAMES, extend=False)
            for row in self.cur.fetchall():
                if row["feed.code"]:
                    print(row["feed.code"])
            return 0

        if self.args.list_texts:
            self.execute(lib.QUERY_TEXT_NAMES, extend=False)
            for row in self.cur.fetchall():
                if row["key"]:
                    print(row["key"])
            return 0

        if self.args.list_identifiers:
            self.execute(lib.QUERY_IDENTIFIER_NAMES, extend=False)
            for row in self.cur.fetchall():
                if row["classification.identifier"]:
                    print(row["classification.identifier"])
            return 0

        if self.args.list_taxonomies:
            self.execute(lib.QUERY_TAXONOMY_NAMES, extend=False)
            for row in self.cur.fetchall():
                if row["classification.taxonomy"]:
                    print(row["classification.taxonomy"])
            return 0

        if self.args.list_types:
            self.execute(lib.QUERY_TYPE_NAMES, extend=False)
            for row in self.cur.fetchall():
                if row["classification.type"]:
                    print(row["classification.type"])
            return 0

        if locale.getpreferredencoding() != "UTF-8":
            self.logger.error(
                "The preferred encoding of your locale setting is not UTF-8 "
                "but %s. Exiting.",
                locale.getpreferredencoding(),
            )
            return 1

        if not self.rt.login():
            self.logger.error(
                "Could not login as %r on %r.",
                self.config["rt"]["user"],
                self.config["rt"]["uri"],
            )
            return 2
        else:
            self.logger.info(
                "Logged in as %r on %r.",
                self.config["rt"]["user"],
                self.config["rt"]["uri"],
            )
        try:
            self.execute(lib.QUERY_OPEN_TAXONOMIES)
            taxonomies = [x["classification.taxonomy"] for x in self.cur.fetchall()]
            self.logger.info("All taxonomies: " + ", ".join(taxonomies))
            for taxonomy in taxonomies:
                self.logger.info("Handling taxonomy %r.", taxonomy)
                if (
                    taxonomy not in lib.SUBJECT or lib.SUBJECT[taxonomy] is None
                ) and not self.subject:
                    self.logger.error("No subject defined for %r." % taxonomy)
                    continue
                self.execute(lib.QUERY_OPEN_EVENT_REPORTS_BY_TAXONOMY, (taxonomy,))
                report_ids = [x["rtir_report_id"] for x in self.cur.fetchall()]
                self.execute(lib.QUERY_OPEN_EVENT_IDS_BY_TAXONOMY, (taxonomy,))
                event_ids = [x["id"] for x in self.cur.fetchall()]
                if self.subject:
                    subject = self.subject
                else:
                    subject = "%s %s incidents on %s" "" % (
                        len(event_ids),
                        lib.SUBJECT[taxonomy],
                        datetime.datetime.now().strftime("%Y-%m-%d"),
                    )

                if self.dryrun:
                    self.logger.info("Simulate creation of incident.")
                    incident_id = -1
                else:
                    incident_id = self.rt.create_ticket(
                        Queue="Incidents",
                        Subject=subject,
                        Owner=self.config["rt"]["user"],
                    )
                    if incident_id == -1:
                        self.logger.error("Could not create Incident %r.", subject)
                        continue

                    self.logger.info("Created Incident %s." % incident_id)
                    # XXX TODO: distinguish between national and other constituencies
                    self.rt.edit_ticket(
                        incident_id,
                        CF_Classification=taxonomy,
                        # CF_Constituency='NATIONAL',
                        CF_Function="IncidentCoord",
                    )

                for report_id in report_ids:
                    if not self.dryrun and not self.rt.edit_link(
                        report_id, "MemberOf", incident_id
                    ):
                        self.logger.error(
                            "Could not link Incident to Incident Report: (%d -> %d).",
                            incident_id,
                            report_id,
                        )
                        continue
                    elif self.dryrun:
                        self.logger.info(
                            "Would have linked Incident Report %d to Incident.",
                            report_id,
                        )

                self.executemany(
                    "UPDATE {events} SET rtir_incident_id = %s WHERE id = %s",
                    [(incident_id, event_id) for event_id in event_ids],
                    extend=False,
                )
                self.con.commit()
                self.logger.info("Linked events to incident.")

                if not self.dryrun:
                    self.execute(
                        lib.QUERY_DISTINCT_CONTACTS_BY_INCIDENT, (incident_id,)
                    )
                else:
                    self.execute(
                        lib.DRY_QUERY_DISTINCT_CONTACTS_BY_TAXONOMY, (taxonomy,)
                    )

                contacts = [x["source.abuse_contact"] for x in self.cur.fetchall()]
                inv_results = []

                for contact in contacts:
                    self.logger.info("Handling contact " + contact)
                    if not self.dryrun:
                        self.execute(
                            lib.QUERY_EVENTS_BY_ASCONTACT_INCIDENT,
                            (
                                incident_id,
                                contact,
                            ),
                        )
                    else:
                        self.execute(
                            lib.DRY_QUERY_EVENTS_BY_ASCONTACT_TAXONOMY,
                            (
                                taxonomy,
                                contact,
                            ),
                        )
                    data = self.cur.fetchall()
                    results = self.send(taxonomy, contact, data, incident_id)
                    if results:
                        inv_results.append(results)
                    else:
                        return 1

                if all(inv_results):
                    try:
                        if not self.dryrun and not self.rt.edit_ticket(
                            incident_id, Status="resolved"
                        ):
                            self.logger.error(
                                "Could not close incident %d.", incident_id
                            )
                    except IndexError:
                        # Bug in RT/python-rt
                        pass
                else:
                    self.logger.warn(
                        "Not all investigations completed -> Can't resolve "
                        "incident %d.",
                        incident_id,
                    )
            self.execute(lib.QUERY_HALF_PROC_INCIDENTS)
            query = [
                (x["rtir_incident_id"], x["classification.taxonomy"])
                for x in self.cur.fetchall()
            ]
            self.logger.info("All half processed incidents and taxonomy: " + str(query))
            for incident_id, taxonomy in query:
                self.logger.info(
                    "Handling incident %d and taxonomy %r.", incident_id, taxonomy
                )
                if (
                    taxonomy not in lib.SUBJECT or lib.SUBJECT[taxonomy] is None
                ) and not self.args.subject:
                    self.logger.error("No subject defined for %r." % taxonomy)
                    continue

                self.execute(lib.QUERY_DISTINCT_CONTACTS_BY_INCIDENT, (incident_id,))
                contacts = [x["source.abuse_contact"] for x in self.cur.fetchall()]

                inv_results = []
                for contact in contacts:
                    self.logger.info("Handling contact " + contact)
                    self.execute(
                        lib.QUERY_EVENTS_BY_ASCONTACT_INCIDENT,
                        (
                            incident_id,
                            contact,
                        ),
                    )
                    data = self.cur.fetchall()
                    results = self.send(taxonomy, contact, data, incident_id)
                    if results:
                        inv_results.append(results)
                    else:
                        return 1

                if all(inv_results):
                    # This is a terrible solution, but looks like RT has a race-condition causing
                    # re-opening incidents if we are too quick.
                    sleep(5)
                    try:
                        if not self.dryrun and not self.rt.edit_ticket(
                            incident_id, Status="resolved"
                        ):
                            self.logger.error(
                                "Could not close incident %d.", incident_id
                            )
                    except IndexError:
                        # Bug in RT/python-rt
                        pass
                else:
                    self.logger.warn(
                        "Not all investigations completed -> Can't resolve "
                        "incident %d.",
                        incident_id,
                    )
                    return 1
            return 0

        finally:
            self.rt.logout()

    def query_get_text(self, text_id):
        self.execute(
            lib.QUERY_GET_TEXT.format(texttab=self.config["database"]["text_table"]),
            (text_id,),
            extend=False,
        )

    def get_text(self, text_id):
        text = None
        if self.boilerplate:  # get id from parameter
            text_id = self.boilerplate
        self.query_get_text(text_id)
        if self.cur.rowcount:
            text = self.cur.fetchall()[0]["body"]
        if not text:  # if all failed, get the default
            self.query_get_text(self.config["database"]["default_key"])
            if self.cur.rowcount:
                text = self.cur.fetchall()[0]["body"]
            else:
                self.logger.error("Default text not found!")
                return None

        return text

    def shrink_dict(self, d):
        if not self.compress_csv:
            return d
        keys = list(d[0].keys())
        empty = dict(zip(keys, [True] * len(keys)))
        for line in d:
            for key, value in line.items():
                if value is not None:
                    empty[key] = False
        return [{k: v for k, v in dicti.items() if not empty[k]} for dicti in d]

    def _preprocess_row(self, row):
        description = row.get("event_description.text")
        if description:
            self._collected_descriptions.add(description.replace("\\n", "\n"))
            # \\n - encoded new lines
            row["event_description.text"] = description.replace("\n", " ").replace(
                "\\n", " "
            )
        return row

    @property
    @lru_cache()
    def event_description_divider(self):
        divider = None
        self.query_get_text("event-description-divider")
        if self.cur.rowcount:
            divider = self.cur.fetchall()[0]["body"]
        return divider or "\n --- \n"

    def _prepare_descriptions_text(self):
        return self.event_description_divider.join(self._collected_descriptions)

    def send(self, taxonomy, contact, query, incident_id, requestor=None):
        if not query:
            self.logger.error("No data!")
            return False
        if not requestor:
            requestor = contact

        # PREPARATION
        query = self.shrink_dict(query)
        ids = list(str(row["id"]) for row in query)

        if self.subject:
            subject = self.subject
        else:
            subject = "{tax} incidents in your network: {date}" "".format(
                date=datetime.datetime.now().strftime("%Y-%m-%d"),
                tax=lib.SUBJECT[taxonomy],
            )
        text = self.get_text(taxonomy) or ""
        csvfile = io.StringIO()
        writer = csv.DictWriter(
            csvfile,
            fieldnames=lib.CSV_FIELDS,
            quoting=csv.QUOTE_MINIMAL,
            delimiter=str(";"),
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        query_unicode = query
        self._collected_descriptions = set()
        writer.writerows(self._preprocess_row(row) for row in query)
        event_descriptions = self._prepare_descriptions_text()
        text = text.format(event_descriptions=event_descriptions)

        # note this might contain UTF-8 chars! let's ignore utf-8 errors. sorry.
        attachment_text = csvfile.getvalue()
        attachment_lines = attachment_text.splitlines()

        if self.verbose:
            self.logger.info(text)

        showed_text = (
            "=" * 100
            + """
To: {to}
Subject: {subj}

{text}
    """.format(
                to=requestor, subj=subject, text=text
            )
        )
        showed_text_len = showed_text.count("\n")

        # SHOW DATA
        if self.table_mode:
            if self.quiet:
                height = 80  # assume anything for quiet mode
            else:
                height = lib.getTerminalHeight() - 3 - showed_text_len
            csvfile.seek(0)
            if len(query) > height:
                with tempfile.NamedTemporaryFile(mode="w+") as handle:
                    handle.write(showed_text + "\n")
                    handle.write(
                        tabulate.tabulate(query, headers="keys", tablefmt="psql")
                    )
                    handle.seek(0)
                    subprocess.call(["less", handle.name])
            else:
                self.logger.info(showed_text)
                self.logger.info(
                    tabulate.tabulate(query_unicode, headers="keys", tablefmt="psql")
                )
        else:
            if self.quiet:
                height = 80
            else:
                height = lib.getTerminalHeight() - 4
            if 5 + len(query) > height:  # cut query too, 5 is length of text
                self.logger.info("\n".join(showed_text.splitlines()[:5]))
                self.logger.info("...")
                self.logger.info("\n".join(attachment_lines[: height - 5]))
                self.logger.info("...")
            elif showed_text_len + len(query) > height > 5 + len(query):
                self.logger.info(
                    "\n".join(showed_text.splitlines()[: height - len(query)])
                )
                self.logger.info("...")
                self.logger.info(attachment_text)
            else:
                self.logger.info(showed_text)
                self.logger.info(attachment_text)
        self.logger.info("-" * 100)

        # MENU
        if self.batch and requestor:
            answer = "s"
        else:
            answer = "q"
            if self.batch:
                self.logger.error("You need to set a valid requestor!")
            else:
                answer = input(
                    "{i}{b}[a]{i}utomatic, {b}[n]{i}ext, {i}{b}[s]{i}end, show "
                    "{b}[t]{i}able, change {b}[r]{i}equestor or {b}[q]{i}uit?{r} "
                    "".format(b=bold, i=myinverted, r=reset)
                ).strip()
        if answer == "q":
            exit(0)
        elif answer == "n":
            return False
        elif answer == "a":
            self.batch = True
        elif answer == "t":
            self.table_mode = bool((self.table_mode + 1) % 2)
            return self.send(taxonomy, contact, query, incident_id, requestor)
        elif answer == "r":
            answer = input(inverted("New requestor address:") + " ").strip()
            if len(answer) == 0:
                requestor = contact
            else:
                requestor = answer
            return self.send(taxonomy, contact, query, incident_id, requestor)
        elif answer != "s":
            self.logger.error("Unknow command %r.", answer)
            return self.send(taxonomy, contact, query, incident_id, requestor)

        if text is None:
            self.logger.error("I won't send with a missing text!")
            return False

        # INVESTIGATION
        if self.dryrun:
            self.logger.info("Simulate creation of investigation.")
            investigation_id = -1
        else:
            investigation_id = self.rt.create_ticket(
                Queue="Investigations",
                Subject=subject,
                Owner=self.config["rt"].get(
                    "investigation_owner", self.config["rt"]["user"]
                ),
                Requestor=requestor,
            )

            if investigation_id == -1:
                self.logger.error("Could not create Investigation %r.", subject)
                return False

            self.logger.info("Created Investigation %d.", investigation_id)
            if not self.rt.edit_link(incident_id, "HasMember", investigation_id):
                self.logger.error("Could not link Investigation to Incident.")
                return False

            self.executemany(
                "UPDATE {events} SET rtir_investigation_id = %s WHERE id = %s",
                [(investigation_id, evid) for evid in ids],
                extend=False,
            )
            self.logger.info("Linked events to investigation.")

        # CORRESPOND
        filename = "%s-%s.csv" % (
            datetime.datetime.now().strftime("%Y-%m-%d"),
            taxonomy,
        )
        if self.zipme or len(query) > self.config["rt"]["zip_threshold"]:
            attachment = io.BytesIO()
            ziphandle = zipfile.ZipFile(
                attachment, mode="w", compression=zipfile.ZIP_DEFLATED
            )
            data = csvfile.getvalue()
            ziphandle.writestr("events.csv", data)
            ziphandle.close()
            attachment.seek(0)
            filename += ".zip"
            mimetype = "application/octet-stream"
        else:
            attachment = csvfile
            attachment.seek(0)
            mimetype = "text/csv"

        try:
            # TODO: CC
            if self.dryrun:
                self.logger.info("Simulate creation of correspondence.")
            else:
                correspond = self.rt.reply(
                    investigation_id,
                    text=text,
                    files=[(filename, attachment, mimetype)],
                )
                if not correspond:
                    self.logger.error("Could not correspond with text and file.")
                    return False
                self.logger.info("Correspondence added to Investigation.")

            self.execute(
                "UPDATE {events} SET sent_at = LOCALTIMESTAMP WHERE "
                "rtir_investigation_id = %s",
                (investigation_id,),
                extend=False,
            )
            self.logger.info("Marked events as sent.")
        except Exception:
            self.con.rollback()
            raise
        else:
            self.con.commit()

            # RESOLVE
            try:
                if not self.dryrun and not self.rt.edit_ticket(
                    investigation_id, Status="resolved"
                ):
                    self.logger.error(
                        "Could not close investigation %d.", investigation_id
                    )
            except IndexError:
                # Bug in RT/python-rt
                pass

        if requestor != contact:
            asns = set(str(row["source.asn"]) for row in query)
            answer = input(
                inverted(
                    "Save recipient {!r} for ASNs {!s}? [Y/n] "
                    "".format(requestor, ", ".join(asns))
                )
            ).strip()
            if answer.strip().lower() in ("", "y", "j"):
                self.executemany(
                    lib.QUERY_UPDATE_CONTACT,
                    [(requestor, asn) for asn in asns],
                    extend=False,
                )
                self.con.commit()
                if self.cur.rowcount == 0:
                    self.query_insert_contact(asns=asns, contact=requestor)

        return True

    def query_insert_contact(self, contact, asns):
        user = os.environ["USER"]
        time = datetime.datetime.now().strftime("%c")
        comment = "Added by {user} @ {time}".format(user=user, time=time)
        self.executemany(
            lib.QUERY_INSERT_CONTACT,
            [(asn, contact, comment) for asn in asns],
            extend=False,
        )
        self.con.commit()


def main():
    controller = IntelMQCLIContoller()
    sys.exit(controller.run(sys.argv[1:]))


if __name__ == "__main__":
    main()
