import unicodecsv

engagement_filename = 'resource/daily_engagement.csv'
submissions_filename = 'resource/project_submissions.csv'
with open(engagement_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)
print daily_engagement[0]
with open(submissions_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)
print project_submissions[0]