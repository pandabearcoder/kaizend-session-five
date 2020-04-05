from contextlib import contextmanager


class Job:

    def __init__(self, label):
        self.label = label

    def load(self, url):
        self.target_url = url
        return self

    def find(self, selector):
        self.selector = selector
        return self

    def save(self, save_file):
        self.save_file = save_file
        return self

    def complete(self):
        print(f'[START {self.label}]')
        print(f'TARGET_URL = {self.target_url}')
        print(f'SELECTOR = {self.selector}')
        print(f'SAVE_FILE = {self.save_file}')
        print(f'[END {self.label}]')


@contextmanager
def scraping_job(label):
    job = Job(label)
    yield job


def main():
    with scraping_job('Job 1') as job:
        job.load('<url>').find('<target>').save('<filename>').complete()


if __name__ == '__main__':
    main()
