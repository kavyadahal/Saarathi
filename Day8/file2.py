from pathlib import Path

p = Path("data")/"notes.txt"
p.exists() #True/False  
p.write_text("Hello file")




