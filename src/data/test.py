import matplotlib.pyplot as plt

# Sample data
time_intervals = ['15 min', '1 hr', '4 hr', '6 hr', '12 hr', '18 hr', '>24 hr']
tickets = [10, 25, 35, 20, 15, 10, 5]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(time_intervals, tickets, color='skyblue')

# Adding titles and labels
plt.title('TT AGEING OPEN TICKET')
plt.xlabel('Time Intervals')
plt.ylabel('Number of Tickets')

# Display the chart
plt.show()
