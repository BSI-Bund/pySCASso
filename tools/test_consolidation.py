"""This compares test cases of different versions. If they are equal, we only symlink a new py file
 to the old similar version"""
import argparse
import glob
import os
import sqlite3
import subprocess
import sys
from dataclasses import dataclass


class ChangeDirectoryContextManager:
    """Context manager for changing the current working directory"""
    def __init__(self, new_path):
        self.new_path = os.path.expanduser(new_path)
        self.saved_path = ""

    def __enter__(self):
        self.saved_path = os.getcwd()
        os.chdir(self.new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.saved_path)


@dataclass
class SCASTest:
    """Dataclass holding all relevant information about a test case"""
    test_id: str
    section_nr: str
    section_title: str
    threat_refs: str
    test_name: str
    req_name: str
    req_ref: str
    req_desc: str
    purpose: str
    pre_conditions: str
    exec_steps: str
    exp_results: str
    evidence_for: str


DB_CONNECTION = None


def get_db():
    """Returns a db connection to our scas database"""
    global DB_CONNECTION
    if DB_CONNECTION is None:
        DB_CONNECTION = sqlite3.connect("scas.db")
    return DB_CONNECTION


def main():
    """Main function"""
    argp = argparse.ArgumentParser()
    argp.add_argument("-n", "--new_release_folder", type=str, required=True)
    argp.add_argument("-o", "--old_release_folder", type=str, required=True)

    args = argp.parse_args()

    filenames = []

    for filename in glob.iglob(args.new_release_folder + "**/*.py", recursive=True):
        filenames.append(filename)

    for filename in glob.iglob(args.old_release_folder + "**/*.py", recursive=True):
        filenames.append(filename)

    new_rel = args.new_release_folder.split("/")[2]
    old_rel = args.old_release_folder.split("/")[2]

    releases = {}

    for filename in filenames:
        short_filename = filename.replace("test_", "")
        release = short_filename.split("/")[2]
        doc_num = short_filename.split("/")[3].split("_")[0]
        py_file = short_filename.split("/")[4]
        version = py_file.split("_")[1]
        section = py_file.split("_", 2)[2].replace(".py", "").replace("_", ".")

        if release not in releases:
            releases[release] = {}

        if doc_num not in releases[release]:
            releases[release][doc_num] = {}

        if section not in releases[release][doc_num]:
            doc_id = f"{doc_num}-{version}"
            with get_db() as con:
                row = con.execute("SELECT * FROM test INNER JOIN test_to_doc USING(test_id) WHERE "
                                  "doc_id==? AND section_nr==?", (doc_id, section, ))
                row = row.fetchone()
                as_list = list(row)
                releases[release][doc_num][section] = (SCASTest(*tuple(as_list)[0:-1]), filename)
        else:
            print(f"Duplicate section {section} in {doc_num + version}")
            sys.exit(-1)

    for doc in releases[new_rel]:
        for section in releases[new_rel][doc]:

            (new_test, new_test_file) = releases[new_rel][doc][section]

            try:
                (old_test, old_test_file) = releases[old_rel][doc][section]

                # we assume tests are equal, if test steps, expected results and pre conditions did
                # not change
                if new_test.test_id == old_test.test_id or \
                   new_test.exec_steps == old_test.exec_steps and \
                   new_test.exp_results == old_test.exp_results and \
                   new_test.pre_conditions == old_test.pre_conditions:
                    with ChangeDirectoryContextManager(
                        f"{'/'.join(new_test_file.split('/')[0:-1])}"):
                        if os.path.exists(new_test_file.split('/')[-1]):
                            os.remove(new_test_file.split('/')[-1])
                        cmd = (f"ln -s -r ../{old_test_file.replace('/tests', '')} "
                               f"{new_test_file.split('/')[-1]}".split())
                        subprocess.call(cmd)
                        print(f"Linking {cmd}")

            except RuntimeError:
                print(f"Test    {new_test_file} seams unique")


if __name__ == "__main__":
    main()
