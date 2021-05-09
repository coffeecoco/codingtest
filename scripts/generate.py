from jinja2 import Environment, FileSystemLoader
import sys
import argparse
import json



def generate_template(
    service_name,
    version,
    git_commit_sha,
    description,
    log_level,
):
    env = Environment(
        loader=FileSystemLoader("./"),
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=True,
    )
    template = env.get_template("cicd/build/environment.py.j2")
    output = template.render(
        service_name=service_name,
        version=version,
        git_commit_sha=git_commit_sha,
        description=description,
        log_level=log_level

    )
    print(output)
    with open("src/api/environment.py", "w") as yaml_file:
        yaml_file.write(output)


def process_args():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-sn", "--service_name", help="service_name", default="None"
        )
        parser.add_argument(
            "-v",
            "--version",
            help="version",
            default="None",
        )
        parser.add_argument(
            "-gsha", "--git_commit_sha", help="git_commit_sha", default="None"
        )
        parser.add_argument(
            "-l", "--log_level", help="log_level", default="None"
        )

        return parser.parse_args()
    except:
        e = sys.exc_info()[0]
        print(e)


def main():
    with open('metadata.json') as f:
        metadata = json.load(f)
    args = process_args()
    service_name = args.service_name
    version = metadata['version']
    git_commit_sha = args.git_commit_sha
    description = metadata['description']
    log_level = metadata['log_level']

    generate_template(
        service_name,
        version,
        git_commit_sha,
        description,
        log_level,
    )


if __name__ == "__main__":
    main()
