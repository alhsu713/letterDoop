from datetime import date

# https://docs.google.com/spreadsheets/d/1yDYp8zITpiHhLLeXDpLD53ScFeqwYkO7i-Te_64qfrk/edit#gid=268919053
def main():
  # 8 questions, quarterly cadence
  months = [0,3,6,9]
  date = 15
  numQ = 8
  today = date.today()
  if(months.indexOf(today.getMonth()) != -1 and today.getDay() == date):
    return
    
  

