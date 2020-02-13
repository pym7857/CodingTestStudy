def solution(food_times, k):
    minf = min(food_times)
    Mlenf = len(food_times)
    lenf= len(food_times)
    sumf = sum(food_times)
    sort_food_times=list(set(food_times))
    minTotal=minf*lenf
    
    if minTotal>k:
        answer=(k%lenf)+1
    elif sumf <=k:
        answer = -1
    else:
        i=1
        k-=minTotal
        lenf-=food_times.count(sort_food_times[0]) 
        minTotal=(sort_food_times[1]-sort_food_times[0])*lenf
        while True:
            if  minTotal<k:
                k-=minTotal
                lenf-=food_times.count(sort_food_times[i])
                i+=1
                minTotal=(sort_food_times[i]-sort_food_times[i-1])*lenf
            else:
                minf=sort_food_times[i-1]
                break  
        i=0
        j=food_times.index(minf)
        while i<k:
            if food_times[j%Mlenf]>minf:
                food_times[j%Mlenf]-=1
                i+=1
                j+=1
            else:
                j+=1
        while food_times[j%Mlenf]<=minf:
            j+=1
        answer=(j%Mlenf)+1
    return answer
