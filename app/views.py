from django.shortcuts import render, redirect
from .models import Goal, Grade, Training
from .forms import  AddClimb, AddTraining
from django.http.response import JsonResponse


#home page
def home(response):
    #check if user is logged in 
    if response.user.is_authenticated:
        #if method is POST
        if response.method == "POST":
            #if new training is added
            if response.POST.get("newtraining"):
                #get data from the form
                form = AddTraining(response.POST)
                #if data is okay, add it to the database
                if form.is_valid():
                    d = form.cleaned_data["date"]
                    newdata = Training(date=d)
                    newdata.save()
                    response.user.training.add(newdata)
                    
            #if new climbed route is added
            elif response.POST.get("newclimb"):
                #get data from the form
                form = AddClimb(response.POST)
                #if data is okay, add it to the database
                if form.is_valid():
                    d = form.cleaned_data["date"]
                    g = form.cleaned_data["grade"]
                    newdata = Grade(date=d, grade=g)
                    newdata.save()
                    response.user.grade.add(newdata)

            return redirect("/")

    training_form = AddTraining()
    climb_form = AddClimb()
    return render(response, "app/home.html", {"training_form": training_form, "climb_form": climb_form})


#function for displaying training sessions per week data
def data_chart(response):
    #get all trainings if user is authenticated
    if response.user.is_authenticated:
        all_trainings = response.user.training.all().order_by('-date')
        
        #if there is no data, return none
        if len(all_trainings) < 1:
            return JsonResponse(data={
                'labels': None,
                'data': None,
            })
        #determine how many weeks of training data we want to display
        totalweeks = 5

        #initialize variables for keeping track on how many trainings each week has
        recent_year, recent_week, recent_week_day = all_trainings[0].date.isocalendar()
        i = 0
        training_per_week = [0, 0, 0, 0, 0]
        week_num = [0, 0, 0, 0, 0]
        week_num[4] = recent_week

        #calculate trainings per week for last few weeks
        for item in all_trainings:
            year, week, day = item.date.isocalendar()
            #if we are on the same week, add one training session
            if week == recent_week:
                training_per_week[4 - i] += 1

            #if not, we moved to the next week
            else:
                totalweeks -= 1
                if totalweeks == 0:
                    break
                i += 1
                #add this training to the new week
                training_per_week[4 - i] += 1
                week_num[4 - i] = week
                recent_week = week
        
        #return data for graphs
        return JsonResponse(data={
            'labels': week_num,
            'data': training_per_week,
        })
    #if user is not authenticated, return empty data
    return JsonResponse(data={
        'labels': None,
        'data': None,
    })

#function for displaying hardest climbs each week
def grade_chart(response):
    #get all grades if user is authenticated
    if response.user.is_authenticated:
        all_grades = response.user.grade.all().order_by('-date')

        #if there is no data, return none
        if len(all_grades) < 1:
            return JsonResponse(data={
                'labels': None,
                'data': None,
            })

        #determine how many weeks of climbing data we want to display
        totalweeks = 5

        #initialize variables for keeping track on how many trainings each week has
        recent_year, recent_week, recent_week_day = all_grades[0].date.isocalendar()
        i = 0
        highest_per_week = [0, 0, 0, 0, 0]
        week_num = [0, 0, 0, 0, 0]
        week_num[4] = recent_week

        #calculate trainings per week for last few weeks
        for item in all_grades:
            year, week, day = item.date.isocalendar()
            #if the current grade is higher than current week's highest grade
            if week == recent_week:
                if item.grade > highest_per_week[4-i]:
                        highest_per_week[4 - i] = item.grade
                    
            #if we moved to the next week
            if week != recent_week:
                totalweeks -= 1
                if totalweeks == 0:
                    break
                i += 1
                week_num[4 - i] = week
                recent_week = week
                #set new highest grade for this new week
                highest_per_week[4 - i] = item.grade
        
        #return data for graphs
        return JsonResponse(data={
            'labels': week_num,
            'data': highest_per_week,
        })
    
    #if user is not authenticated, return empty data
    return JsonResponse(data={
        'labels': None,
        'data': None,
    })

def goals(response):
    #check if user is logged in 
    if response.user.is_authenticated:
        #get all goals user has
        all_goals = response.user.goal.all()

        #if we get POST request
        if response.method == "POST":
            #if the "Add Goal" button was clicked
            if response.POST.get("addgoal"):
                goal_title = response.POST.get("newgoal")
                # if input isn't empty, save it and add to user's goal database
                if len(goal_title) >= 1:
                    new_goal = Goal(title=goal_title, done=False)
                    new_goal.save()
                    response.user.goal.add(new_goal)

            #if the "Complete goals" button was clicked
            if response.POST.get("completegoals"):
                for item in all_goals:
                    if response.POST.get("c" + str(item.goalId)) == "clicked":
                        item.done = True

                    item.save()

            #if the "Delete goals" button was clicked
            if response.POST.get("deletegoals"):
                for item in all_goals:
                    if response.POST.get("c" + str(item.goalId)) == "clicked":
                        item.delete()
                return redirect("/goals")


        #initialize lists of completed and uncompleted goals
        completed = []
        uncompleted = []
        #put goals to those lists
        for item in all_goals:
            if item.done == True:
                completed.append(item)
            else:
                uncompleted.append(item)

        return render(response, "app/goals.html", {"goal_list":uncompleted, "done_list":completed})
            
    return render(response, "app/goals.html", {})

#simple account page with some stats and login/logout stuff
def account(response):
    #check if logged in
    if response.user.is_authenticated:
        #get all data for user
        total_trainings = len(response.user.training.all())
        all_grades = response.user.grade.all()
        #check highest grade
        highest = 0
        for i in all_grades:
            if i.grade > highest:
                highest = i.grade
        return render(response, "app/account.html", {"total":total_trainings, "highest": highest})

    return render(response, "app/account.html")

