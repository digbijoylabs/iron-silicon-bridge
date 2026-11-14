// CORRECT PATTERN: The Transactional Outbox
@Transactional
public void processOrder(Order order) {
    // Step 1: Write to local database
    orderRepository.save(order);
    
    // Step 2: Write event to local outbox table
    // IN THE SAME TRANSACTION
    OutboxEvent event = new OutboxEvent("Order", order);
    outboxRepository.save(event);
}
