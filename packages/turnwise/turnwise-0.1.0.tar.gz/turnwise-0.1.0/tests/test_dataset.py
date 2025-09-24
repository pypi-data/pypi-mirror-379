"""Tests for dataset management."""

from turnwise import Conversation, ConversationDataset, Role, Turn


class TestConversationDataset:
    """Test ConversationDataset class."""

    def test_empty_dataset_creation(self):
        """Test creating an empty dataset."""
        dataset = ConversationDataset()
        assert len(dataset) == 0
        assert list(dataset) == []

    def test_constructor_with_conversations(self):
        """Test constructor with Conversation objects."""
        conv1 = Conversation(turns=[Turn(role=Role.USER, content="Hello")])
        conv2 = Conversation(turns=[Turn(role=Role.USER, content="Hi")])

        dataset = ConversationDataset([conv1, conv2])
        assert len(dataset) == 2
        assert dataset[0] == conv1
        assert dataset[1] == conv2

    def test_constructor_with_dicts(self):
        """Test constructor with dictionary data."""
        data = [
            {"turns": [{"role": "user", "content": "Hello"}], "metadata": {"id": "1"}},
            {"turns": [{"role": "user", "content": "Hi"}], "metadata": {"id": "2"}},
        ]

        dataset = ConversationDataset(data)
        assert len(dataset) == 2
        assert dataset[0].turns[0].content == "Hello"
        assert dataset[1].turns[0].content == "Hi"

    def test_constructor_with_tuples(self):
        """Test constructor with tuple data."""
        data = [("user", "Hello"), ("assistant", "Hi there!")]

        dataset = ConversationDataset(data)
        assert len(dataset) == 1
        assert len(dataset[0].turns) == 2
        assert dataset[0].turns[0].content == "Hello"
        assert dataset[0].turns[1].content == "Hi there!"

    def test_add_single(self):
        """Test adding a single conversation to dataset."""
        dataset = ConversationDataset()

        conv = Conversation(turns=[Turn(role=Role.USER, content="Hello")])

        dataset.add(conv)
        assert len(dataset) == 1
        assert dataset[0] == conv

    def test_add_multiple(self):
        """Test adding multiple conversations to dataset."""
        dataset = ConversationDataset()
        conv1 = Conversation(turns=[Turn(role=Role.USER, content="Hello")])
        conv2 = Conversation(turns=[Turn(role=Role.USER, content="Hi")])

        dataset.add([conv1, conv2])
        assert len(dataset) == 2
        assert dataset[0] == conv1
        assert dataset[1] == conv2

    def test_add_from_dicts(self):
        """Test adding conversations from dictionaries."""
        dataset = ConversationDataset()
        data = [
            {"turns": [{"role": "user", "content": "Hello"}], "metadata": {"id": "1"}},
            {"turns": [{"role": "user", "content": "Hi"}], "metadata": {"id": "2"}},
        ]

        dataset.add(data)
        assert len(dataset) == 2
        assert dataset[0].turns[0].content == "Hello"
        assert dataset[1].turns[0].content == "Hi"

    def test_iteration(self):
        """Test iterating over dataset."""
        conv1 = Conversation(turns=[Turn(role=Role.USER, content="Hello")])
        conv2 = Conversation(turns=[Turn(role=Role.USER, content="Hi")])
        dataset = ConversationDataset([conv1, conv2])

        conversations = list(dataset)
        assert len(conversations) == 2
        assert conversations[0] == conv1
        assert conversations[1] == conv2

    def test_filter_length(self):
        """Test filtering by conversation length."""
        conv1 = Conversation(turns=[Turn(role=Role.USER, content="Hello")])  # 1 turn
        conv2 = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi"),
            ]
        )  # 2 turns
        conv3 = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi"),
                Turn(role=Role.USER, content="How are you?"),
            ]
        )  # 3 turns

        dataset = ConversationDataset([conv1, conv2, conv3])

        # Filter for 2-3 turns
        filtered = dataset.filter_length(min_turns=2, max_turns=3)
        assert len(filtered) == 2
        assert filtered[0] == conv2
        assert filtered[1] == conv3

        # Filter for at least 2 turns
        filtered = dataset.filter_length(min_turns=2)
        assert len(filtered) == 2

        # Filter for at most 2 turns
        filtered = dataset.filter_length(max_turns=2)
        assert len(filtered) == 2

    def test_filter_ratio(self):
        """Test filtering by user turn ratio."""
        # 50% user turns
        conv1 = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi"),
            ]
        )

        # 33% user turns
        conv2 = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi"),
                Turn(role=Role.ASSISTANT, content="How are you?"),
            ]
        )

        # 100% user turns
        conv3 = Conversation(turns=[Turn(role=Role.USER, content="Hello")])

        dataset = ConversationDataset([conv1, conv2, conv3])

        # Filter for 40-60% user turns
        filtered = dataset.filter_ratio(min_user_ratio=0.4, max_user_ratio=0.6)
        assert len(filtered) == 1
        assert filtered[0] == conv1

    def test_stats(self):
        """Test getting dataset statistics."""
        conv1 = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi"),
            ],
            metadata={"session": "1"},
        )

        conv2 = Conversation(
            turns=[
                Turn(role=Role.USER, content="How are you?"),
                Turn(role=Role.ASSISTANT, content="I'm good!"),
                Turn(role=Role.USER, content="Great!"),
            ],
            expected_output="Good conversation",
        )

        dataset = ConversationDataset([conv1, conv2])
        stats = dataset.stats()

        assert stats["total_conversations"] == 2
        assert stats["total_turns"] == 5
        assert stats["average_turns_per_conversation"] == 2.5
        assert stats["min_turns"] == 2
        assert stats["max_turns"] == 3
        assert stats["conversations_with_metadata"] == 1
        assert stats["conversations_with_expected_output"] == 1

    def test_empty_dataset_statistics(self):
        """Test statistics for empty dataset."""
        dataset = ConversationDataset()
        stats = dataset.stats()

        assert stats["total_conversations"] == 0
