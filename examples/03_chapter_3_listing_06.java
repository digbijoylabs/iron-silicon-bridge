// DANGEROUS ANTI-PATTERN: The Dual Write
@Transactional
public void processOrder(Order order) {
    // Step 1: Write to local database
    orderRepository.save(order);
    
    // Step 2: Publish to Message Broker
    messageTemplate.send("orders-topic", order.getId());
}
