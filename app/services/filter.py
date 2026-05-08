def filter_services(services, parsed):

    filtered = []

    for service in services:

        print(f"Checking: {service['name']}")

        # GPU filter
        if parsed.get("gpu"):

            if not service["gpu"]:

                print("Rejected GPU")
                continue

        # Budget filter
        if parsed.get("budget"):

            if service["cost"] > parsed["budget"]:

                print("Rejected Budget")
                continue

        # Latency filter
        if parsed.get("latency"):

            if service["latency"] > parsed["latency"]:

                print("Rejected Latency")
                continue

        print("Accepted")

        filtered.append(service)

    return filtered