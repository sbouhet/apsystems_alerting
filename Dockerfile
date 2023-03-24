# Build Environment: Playwright
FROM mcr.microsoft.com/playwright/python:focal

WORKDIR /app
RUN pip install pytest-playwright
RUN playwright install
COPY aps_website_test.py /app/
