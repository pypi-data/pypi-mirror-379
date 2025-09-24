#!/usr/bin/env python3
"""Example demonstrating the DataFrame-like API for ConversationDataset."""

from turnwise import Conversation, ConversationDataset, Role, Turn


def main():
    print("=== Turnwise DataFrame-like API Example ===\n")

    # 1. Create empty dataset
    print("1. Creating empty dataset:")
    dataset = ConversationDataset()
    print(f"   Empty dataset length: {len(dataset)}")
    print()

    # 2. Create dataset from Conversation objects
    print("2. Creating dataset from Conversation objects:")
    conv1 = Conversation(
        turns=[
            Turn(role=Role.USER, content="Hello"),
            Turn(role=Role.ASSISTANT, content="Hi there!"),
        ]
    )
    conv2 = Conversation(
        turns=[
            Turn(role=Role.USER, content="How are you?"),
            Turn(role=Role.ASSISTANT, content="I'm doing well!"),
        ]
    )

    dataset = ConversationDataset([conv1, conv2])
    print(f"   Dataset length: {len(dataset)}")
    print(f"   First conversation: {dataset[0].turns[0].content}")
    print()

    # 3. Create dataset from dictionaries
    print("3. Creating dataset from dictionaries:")
    dict_data = [
        {
            "turns": [
                {"role": "user", "content": "What's the weather like?"},
                {
                    "role": "assistant",
                    "content": "I can't check the weather, but I can help you find weather apps!",
                },
            ],
            "metadata": {"topic": "weather"},
        },
        {
            "turns": [
                {"role": "user", "content": "Tell me a joke"},
                {
                    "role": "assistant",
                    "content": "Why don't scientists trust atoms? Because they make up everything!",
                },
            ],
            "metadata": {"topic": "humor"},
        },
    ]

    dataset = ConversationDataset(dict_data)
    print(f"   Dataset length: {len(dataset)}")
    print(f"   First conversation topic: {dataset[0].metadata['topic']}")
    print()

    # 4. Create dataset from tuples
    print("4. Creating dataset from tuples:")
    tuple_data = [
        ("user", "Hello"),
        ("assistant", "Hi! How can I help?"),
        ("user", "I need help with coding"),
        ("assistant", "I'd be happy to help with coding!"),
    ]

    dataset = ConversationDataset(tuple_data)
    print(f"   Dataset length: {len(dataset)}")
    print(f"   Number of turns in conversation: {len(dataset[0].turns)}")
    print()

    # 5. Using the add method (like pandas append)
    print("5. Using add method to add data:")
    dataset = ConversationDataset()

    # Add single conversation
    dataset.add(conv1)
    print(f"   After adding single conversation: {len(dataset)}")

    # Add multiple conversations
    dataset.add([conv2])
    print(f"   After adding list: {len(dataset)}")

    # Add from dictionaries
    dataset.add(dict_data)
    print(f"   After adding from dicts: {len(dataset)}")
    print()

    # 6. Dataset operations
    print("6. Dataset operations:")
    print(f"   Total conversations: {len(dataset)}")
    print(f"   Statistics: {dataset.stats()}")
    print()

    # 7. Filtering
    print("7. Filtering operations:")
    long_conversations = dataset.filter_length(min_turns=3)
    print(f"   Conversations with 3+ turns: {len(long_conversations)}")

    balanced_conversations = dataset.filter_ratio(
        min_user_ratio=0.3, max_user_ratio=0.7
    )
    print(f"   Balanced conversations: {len(balanced_conversations)}")
    print()

    # 8. Iteration
    print("8. Iterating over dataset:")
    for i, conv in enumerate(dataset):
        print(f"   Conversation {i + 1}: {len(conv.turns)} turns")

    print("\n=== Example completed! ===")


if __name__ == "__main__":
    main()
