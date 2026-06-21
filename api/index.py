from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 212.72,
    "uptime_pct": 98.711,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 143.31,
    "uptime_pct": 97.155,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 128.63,
    "uptime_pct": 97.46,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 150.38,
    "uptime_pct": 97.526,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 131.57,
    "uptime_pct": 99.391,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 218,
    "uptime_pct": 98.154,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 122.51,
    "uptime_pct": 97.753,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 118.14,
    "uptime_pct": 98.734,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 120,
    "uptime_pct": 98.679,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 186.05,
    "uptime_pct": 99.051,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 218.99,
    "uptime_pct": 97.201,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 228.94,
    "uptime_pct": 98.266,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 177.86,
    "uptime_pct": 99.389,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 186.35,
    "uptime_pct": 98.856,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 226.62,
    "uptime_pct": 97.992,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 152.62,
    "uptime_pct": 97.258,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 114.59,
    "uptime_pct": 99.06,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 130.67,
    "uptime_pct": 98.355,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 101.53,
    "uptime_pct": 98.118,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 117.42,
    "uptime_pct": 97.398,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 217.68,
    "uptime_pct": 97.798,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 176.27,
    "uptime_pct": 98.986,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 184.93,
    "uptime_pct": 97.975,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 226.74,
    "uptime_pct": 99.232,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 123.92,
    "uptime_pct": 97.219,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 203.2,
    "uptime_pct": 97.328,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 168.51,
    "uptime_pct": 97.955,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 209.55,
    "uptime_pct": 98.089,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 223.5,
    "uptime_pct": 97.76,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 128.01,
    "uptime_pct": 98.449,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 193.12,
    "uptime_pct": 97.27,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 199.82,
    "uptime_pct": 97.681,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 169.87,
    "uptime_pct": 98.767,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 200.4,
    "uptime_pct": 98.083,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 161.55,
    "uptime_pct": 99.103,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 164.2,
    "uptime_pct": 98.209,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
