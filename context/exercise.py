from contextlib import contextmanager


class Job:
    label = ''
    target_url = ''
    selector = ''
    save_file = ''

    def __init__(self, label):
        self.label = label


@contextmanager
def scraping_job(label):
    job = Job(label)
    yield job
    print(f'[START {job.label}]')
    print(f'TARGET_URL = {job.target_url}')
    print(f'SELECTOR = {job.selector}')
    print(f'SAVE_FILE = {job.save_file}')
    print(f'[END {job.label}]')


def main():
    with scraping_job('Job 1') as job:
        job.target_url = '<url>'
        job.selector = '<selector>'
        job.save_file = '<filename>'

    with scraping_job('Job 2') as job:
        job.target_url = '<url 2>'
        job.selector = '<selector 2>'
        job.save_file = '<filename 2>'


if __name__ == '__main__':
    main()
