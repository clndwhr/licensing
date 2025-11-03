import uuid

def generate_uuidv5(namespace_uuid, name):
    """
    Generate a UUIDv5 based on a namespace UUID and a name string.
    
    Args:
        namespace_uuid: A UUID object or string representing the namespace
        name: A string to generate the UUID from
    
    Returns:
        A UUIDv5 string
    """
    if isinstance(namespace_uuid, str):
        namespace_uuid = uuid.UUID(namespace_uuid)
    
    return str(uuid.uuid5(namespace_uuid, name))

def main():
    # Common namespace UUIDs (you can use these or create your own)
    namespaces = {
        'dns': uuid.NAMESPACE_DNS,      # For domain names
        'url': uuid.NAMESPACE_URL,      # For URLs  
        'oid': uuid.NAMESPACE_OID,      # For ISO OIDs
        'x500': uuid.NAMESPACE_X500     # For X.500 DNs
    }
    
    print("UUIDv5 Generator")
    print("================")
    print()
    
    # Example 1: Using DNS namespace
    domain_name = "example.com"
    uuid_v5_dns = generate_uuidv5(namespaces['dns'], domain_name)
    print(f"UUIDv5 for domain '{domain_name}': {uuid_v5_dns}")
    
    # Example 2: Using URL namespace
    url = "https://example.com/licensing"
    uuid_v5_url = generate_uuidv5(namespaces['url'], url)
    print(f"UUIDv5 for URL '{url}': {uuid_v5_url}")
    
    # Example 3: Using a custom namespace
    # Generate a random UUID to use as namespace
    custom_namespace = uuid.uuid4()
    license_identifier = "megapp-license-2025"
    uuid_v5_custom = generate_uuidv5(custom_namespace, license_identifier)
    print(f"UUIDv5 for license '{license_identifier}' with custom namespace:")
    print(f"  Namespace: {custom_namespace}")
    print(f"  UUIDv5: {uuid_v5_custom}")
    
    print()
    print("Interactive Generator:")
    print("---------------------")
    
    # Interactive input
    print("Choose a namespace:")
    print("1. DNS namespace (for domain names)")
    print("2. URL namespace (for URLs)")
    print("3. Custom namespace (will generate a new one)")
    
    try:
        choice = input("Enter choice (1-3): ").strip()
        name_input = input("Enter the name/string to generate UUID from: ").strip()
        
        if choice == "1":
            selected_namespace = namespaces['dns']
            namespace_name = "DNS"
        elif choice == "2":
            selected_namespace = namespaces['url']
            namespace_name = "URL"
        elif choice == "3":
            selected_namespace = uuid.uuid4()
            namespace_name = f"Custom ({selected_namespace})"
        else:
            print("Invalid choice, using DNS namespace")
            selected_namespace = namespaces['dns']
            namespace_name = "DNS"
        
        result_uuid = generate_uuidv5(selected_namespace, name_input)
        print(f"\nGenerated UUIDv5:")
        print(f"Namespace: {namespace_name}")
        print(f"Name: {name_input}")
        print(f"UUIDv5: {result_uuid}")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()