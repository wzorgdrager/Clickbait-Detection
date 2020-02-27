from dataset import Dataset

# Import the small and big dataset.
small_dataset = Dataset("datasets/small_training")
big_dataset = Dataset("datasets/big_training")

# Print summaries of both.
small_dataset.print_summary()
big_dataset.print_summary()

# Print the 10th element of both datasets.
small_dataset.get_elements()[10].pretty_print()
big_dataset.get_elements()[10].pretty_print()
