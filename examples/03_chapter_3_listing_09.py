# Pattern: Preventing Cache Stampedes via Distributed Mutex
import time

def get_customer_profile(customer_id):
    cache_key = f"profile:{customer_id}"
    profile = cache.get(cache_key)
    if profile:
        return profile
    
    # Cache Miss. Acquire lock to prevent stampede.
    lock_key = f"lock:profile:{customer_id}"
    if cache.setnx(lock_key, "LOCKED", timeout=5):
        try:
            # Only ONE thread hits the database
            query = "SELECT * FROM customers WHERE id = ?"
            profile = db.query(query, customer_id)
            cache.set(cache_key, profile, ttl=3600)
            return profile
        finally:
            cache.delete(lock_key)
    else:
        # Other threads wait briefly, then retry cache
        time.sleep(0.05)
        return get_customer_profile(customer_id)
