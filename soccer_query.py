import sqlite3

def execute_query(query):
    conn = sqlite3.connect('soccer.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Function to execute a specific query based on user input
def execute_user_query(option):
    if option == 1:
        query = "SELECT COUNT(*) AS TotalPlayers FROM Players;"
    elif option == 2:
        query = "SELECT * FROM Players WHERE RegistrationDate >= date('now', '-1 year');"
    elif option == 3:
        query = """
        SELECT
          r.RefereeID,
          r.FirstName,
          r.LastName,
          COUNT(m.MatchID) AS MatchesOfficiated
        FROM Referees r
        JOIN Matches m ON r.RefereeID = m.RefereeID
        WHERE m.Date >= date('now', '-1 year')
        GROUP BY r.RefereeID
        ORDER BY MatchesOfficiated DESC;
        """
    elif option == 4:
        query = """
        SELECT
            CASE
                WHEN strftime('%Y', DateOfBirth) > strftime('%Y', date('now', '-18 years')) THEN 'Under 18'
                WHEN strftime('%Y', DateOfBirth) BETWEEN strftime('%Y', date('now', '-25 years')) AND strftime('%Y', date('now', '-18 years')) THEN '18-25'
                ELSE 'Over 25'
            END AS AgeGroup,
            COUNT(*) AS PlayerCount
        FROM Players
        GROUP BY AgeGroup;
        """
    elif option == 5:
        query = """
        SELECT
            p.PlayerID,
            p.FirstName,
            p.LastName,
            COUNT(pts.SessionID) AS TrainingSessionsAttended
        FROM Players p
        INNER JOIN PlayersTrainingSessions pts ON p.PlayerID = pts.PlayerID
        INNER JOIN TrainingSessions ts ON pts.SessionID = ts.SessionID
        WHERE ts.Date >= date('now', '-3 months')
        GROUP BY p.PlayerID
        ORDER BY TrainingSessionsAttended DESC;
        """
    elif option == 6:
        query = "SELECT MatchID, HomeTeam, AwayTeam, Date, Time FROM Matches WHERE Date > CURRENT_DATE AND RefereeID IS NULL;"
    elif option == 7:
        query = "SELECT * FROM Matches WHERE Date BETWEEN CURRENT_DATE AND DATE(CURRENT_DATE, '+1 month');"
    elif option == 8:
        query = """
        SELECT
          SUM(t.Price) AS TotalRevenue
        FROM Tickets t
        JOIN Matches m ON t.MatchID = m.MatchID
        WHERE m.Date >= DATE(CURRENT_DATE, '-1 year');
        """
    elif option == 9:
        query = """
        SELECT
          SUM(s.SponsorshipAmount) AS TotalSponsorshipRevenue
        FROM Sponsors s
        JOIN FinancialTransactions ft ON s.SponsorID = ft.SponsorshipID
        WHERE ft.TransactionDate >= DATE(CURRENT_DATE, '-1 year');
        """
    elif option == 10:
        query = """
        SELECT
          TransactionType,
          SUM(Amount) AS TotalAmount
        FROM FinancialTransactions
        WHERE TransactionDate BETWEEN '2023-10-01' AND '2023-12-10'
        GROUP BY TransactionType;
        """
    elif option == 11:
        query = """
        SELECT
          TicketType,
          COUNT(*) AS TicketSales
        FROM Tickets
        GROUP BY TicketType
        ORDER BY TicketSales DESC
        LIMIT 2;
        """
    elif option == 12:
        query = """
        SELECT
          strftime('%Y-%m', SaleDate) AS SaleMonth,
          TicketType,
          COUNT(*) AS TicketSales
        FROM Tickets
        WHERE SaleDate BETWEEN '2023-12-01' AND '2023-12-18'
        GROUP BY SaleMonth, TicketType;
        """
    elif option == 13:
        query = """
        SELECT
          fe.ActivityType,
          COUNT(*) AS ParticipationCount
        FROM FanEngagementActivities fe
        GROUP BY fe.ActivityType
        ORDER BY ParticipationCount DESC;
        """
    elif option == 14:
        query = """
        SELECT
          f.FanID,
          f.FirstName,
          f.LastName,
          COUNT(fe.ActivityID) AS ActivitiesParticipated
        FROM Fans f
        JOIN FanEngagementActivities fe ON f.FanID = fe.FanID
        GROUP BY f.FanID
        ORDER BY ActivitiesParticipated DESC;
        """
    elif option == 15:
        query = """
        SELECT
          strftime('%Y-%m', fe.Date) AS EngagementMonth,
          COUNT(*) AS EngagementCount
        FROM FanEngagementActivities fe
        WHERE fe.Date BETWEEN DATE(CURRENT_DATE, '-1 year') AND CURRENT_DATE
        GROUP BY EngagementMonth;
        """
    elif option == 16:
        query = """
        SELECT
        (SELECT SUM(Amount) FROM FinancialTransactions) AS TotalRevenue,
        (SELECT SUM(SponsorshipAmount) FROM Sponsors) AS TotalSponsor
        """

    else:
        print("Invalid option. Please choose a valid option.")
        return

    result = execute_query(query)
    print("\nQuery Result:")
    for row in result:
        print(row)

# Function to display menu and get user input
def display_menu():
    print("\nChoose an option:")
    print("1. Total number of players")
    print("2. Players registered in the this year")
    print("3. Referees who officiated the most matches this season")
    print("4. Distribution of player registrations based on age groups")
    print("5. Players who attended the most training sessions in the last quarter")
    print("6. Upcoming matches without assigned referees")
    print("7. Report on match schedules for the next month")
    print("8. Total revenue generated from ticket sales in the last fiscal year")
    print("9. Total sponsorship revenue generated so far this year")
    print("10. Breakdown of financial transactions for a specific time period")
    print("11. Ticket type with the highest sales volume")
    print("12. Trends or patterns in ticket sales for special events")
    print("13. Most successful fan engagement activities in terms of participation")
    print("14. Fans who are actively engaging with the organization's activities")
    print("15. How has fan engagement changed over the past year?")
    print("16. What is the overall financial health of the organization?")
    print("0. Exit")

    option = int(input("Enter the option number: "))
    return option

if __name__ == "__main__":
    while True:
        user_option = display_menu()

        if user_option == 0:
            print("Exiting the program. Goodbye!")
            break

        execute_user_query(user_option)
