from services.correlator import detect_clusters

clusters = detect_clusters()

if clusters:
    print(f"Found {len(clusters)} cluster(s):")
    for i, cluster in enumerate(clusters):
        print(f"\nCluster {i+1} — {len(cluster)} reports:")
        for r in cluster:
            print(f"  [{r['label']}] {r['message'][:60]} @ {r['location_name']}")
else:
    print("No clusters detected in the last 2 hours.")