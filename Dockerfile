FROM python:3.8
EXPOSE 8080
WORKDIR /app
COPY . ./
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit", "run", "0_💰_IamRich_Financial_Advisor.py", "--server.port=8080", "--server.address=0.0.0.0"]

