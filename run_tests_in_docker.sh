
docker run \
--env-file variables_local_docker.sh \
--env-file credentials_local_docker.env \
-v /Users/admas/Projects/teaching/QA-LIVE/qa-bootcamp-framework/ssqatest:/automation/ssqatest \
--platform linux/amd64 \
try2 tests -m tcid13 --color=yes


# --color=yes