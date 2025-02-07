#!/bin/sh

ip route del default
ip route add default via 192.168.2.20

# Initialize retry counter
retry_count=0

# Run the dig command in a while loop until a response is received
while true; do
    # Increment retry counter
    retry_count=$((retry_count + 1))
    
    # Execute the dig command and store the output
    output=$(dig @127.0.0.1 www.example.com)
    
    # Extract the DNS query ID
    query_id=$(echo "$output" | grep -oP ";; ->>HEADER<<- .* id: \K\d+")
    
    # Check if the output contains a valid response
    if echo "$output" | grep -q "ANSWER SECTION"; then
        echo "Received a response:"
        echo "DNS Query ID: $query_id"
        echo "Retry Count: $retry_count"
        echo "$output"
        break
    else
        echo "No response yet. Retrying... (Retry Count: $retry_count, Last Query ID: $query_id)"
    fi

    # Optional: Add a delay between retries
    sleep 0.1
done

# Keep the script running indefinitely (equivalent to 'tail -f /dev/null')
tail -f /dev/null
