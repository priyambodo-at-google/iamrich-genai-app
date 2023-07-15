#/bin/bash
docker tag iamrich-app gcr.io/work-mylab-machinelearning/iamrich-app
gcloud auth configure-docker
docker push gcr.io/work-mylab-machinelearning/iamrich-app
gcloud run deploy iamrich-app \
  --image gcr.io/work-mylab-machinelearning/iamrich-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated