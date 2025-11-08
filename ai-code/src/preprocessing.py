import re
import pandas as pd

class TicketProcessor:
    def __init__(self, input_file, output_file):
        self.df = pd.read_csv(input_file)
        self.output_file = output_file
    
    def clean_text(self, text):
        return re.sub(r"[^a-zA-Z\s]", "", text.lower()).strip()
    
    def process_and_save(self):
        self.df["clean_text"] = self.df["ticket_text"].apply(self.clean_text)
        self.df.to_csv(self.output_file, index=False)

if __name__ == "__main__":
    processor = TicketProcessor("data/raw/tickets6.csv", "data/processed/preprocessed_tickets6.csv")
    processor.process_and_save()
    print(f"Preprocessed data saved to '{processor.output_file}'.")
