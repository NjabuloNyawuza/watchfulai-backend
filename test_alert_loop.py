from services.correlator import detect_clusters
from services.alerter import send_cluster_alert

print("Scanning for clusters...")
clusters = detect_clusters()

if not clusters:
    print("No clusters found. Try sending 2 WhatsApp messages to your sandbox first.")
else:
    print(f"Found {len(clusters)} cluster(s). Firing alerts...")
    for i, cluster in enumerate(clusters):
        print(f"\nCluster {i+1} — {len(cluster)} reports")
        send_cluster_alert(cluster)
    print("\nDone. Check your WhatsApp.")
    