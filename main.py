from fastapi import FastAPI, HTTPException
import requests
import os
import base64
from dotenv import load_dotenv
from fastapi import Request

load_dotenv()

app = FastAPI()

DOMAIN = os.environ.get("DOMAIN")
API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("API_SECRET")

@app.get("/api/records/")
async def get_domain_records():
    if not DOMAIN or not API_KEY or not SECRET:
        raise HTTPException(status_code=500, detail="Environment variables not properly configured.")

    url = f"https://api.godaddy.com/v1/domains/{DOMAIN}/records"

    auth_string = f"{API_KEY}:{SECRET}"
    headers = {"Authorization": f"sso-key {auth_string}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/records/{name}")
async def get_domain_records(name):
    if not DOMAIN or not API_KEY or not SECRET:
        raise HTTPException(status_code=500, detail="Environment variables not properly configured.")

    url = f"https://api.godaddy.com/v1/domains/{DOMAIN}/records/CNAME/{name}"

    auth_string = f"{API_KEY}:{SECRET}"
    headers = {"Authorization": f"sso-key {auth_string}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/records/{name}")
async def get_domain_records(name):
    if not DOMAIN or not API_KEY or not SECRET:
        raise HTTPException(status_code=500, detail="Environment variables not properly configured.")

    url = f"https://api.godaddy.com/v1/domains/{DOMAIN}/records/CNAME/{name}"

    auth_string = f"{API_KEY}:{SECRET}"
    headers = {"Authorization": f"sso-key {auth_string}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/api/records/{name}")
async def get_domain_records(name):
    if not DOMAIN or not API_KEY or not SECRET:
        raise HTTPException(status_code=500, detail="Environment variables not properly configured.")

    url = f"https://api.godaddy.com/v1/domains/{DOMAIN}/records/CNAME/{name}"

    auth_string = f"{API_KEY}:{SECRET}"
    headers = {"Authorization": f"sso-key {auth_string}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))