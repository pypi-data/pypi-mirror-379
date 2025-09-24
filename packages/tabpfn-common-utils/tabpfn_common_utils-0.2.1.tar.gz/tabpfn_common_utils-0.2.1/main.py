from tabpfn_common_utils.telemetry.core.service import ProductTelemetry
from tabpfn_common_utils.telemetry.core.events import ModelEventMetadata, AggregatedModelEvent

if __name__ == "__main__":
    telemetry= ProductTelemetry()
    
    # Generate 100 examples of ModelEventMetadata
    examples = []
    
    # Create diverse examples with different tasks, sizes, and durations
    import random
    
    for i in range(100):
        # Alternate between classification and regression tasks
        task = "classification" if i % 2 == 0 else "regression"
        
        # Generate realistic dataset sizes
        num_rows = random.randint(100, 50000)
        num_columns = random.randint(5, 200)
        
        # Generate realistic duration in milliseconds (10ms to 30 seconds)
        duration_ms = random.randint(10, 30000)
        
        example = ModelEventMetadata(
            task=task,
            num_rows=num_rows,
            num_columns=num_columns,
            duration_ms=duration_ms
        )
        
        examples.append(example)
    
    # Print first 10 examples to verify
    print(f"Generated {len(examples)} ModelEventMetadata examples")
    for i, example in enumerate(examples[:10]):
        print(f"Example {i+1}: {example}")

    telemetry.capture(AggregatedModelEvent(payload=examples))
    pass