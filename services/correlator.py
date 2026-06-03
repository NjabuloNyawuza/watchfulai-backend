from database import get_db
from datetime import datetime, timedelta
import math

RADIUS_METRES = 200
TIME_WINDOW_HOURS = 2
CLUSTER_THRESHOLD = 2  # minimum reports to trigger alert

def haversine(lat1, lng1, lat2, lng2):
    R = 6371000  # Earth radius in metres
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)
    a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def get_recent_reports():
    db = get_db()
    cutoff = (datetime.utcnow() - timedelta(hours=TIME_WINDOW_HOURS)).isoformat()
    result = db.table("reports") \
        .select("*") \
        .gte("created_at", cutoff) \
        .in_("label", ["SUSPICIOUS", "EMERGENCY"]) \
        .execute()
    return result.data

def detect_clusters():
    reports = get_recent_reports()
    clusters = []
    used = set()

    for i, report in enumerate(reports):
        if i in used:
            continue
        cluster = [report]
        for j, other in enumerate(reports):
            if i == j or j in used:
                continue
            dist = haversine(
                report["lat"], report["lng"],
                other["lat"], other["lng"]
            )
            if dist <= RADIUS_METRES:
                cluster.append(other)
                used.add(j)
        if len(cluster) >= CLUSTER_THRESHOLD:
            used.add(i)
            clusters.append(cluster)

    return clusters