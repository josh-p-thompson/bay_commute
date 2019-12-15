from django.shortcuts import render

def etas(request):

    context = {
        'stops': [
            {
                'name': 'Richmond', 
                'schedules': [
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    },
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    },
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    },
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    },
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    },
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    },
                ],
            },
            {
                'name': 'Richmond', 
                'schedules': [
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    }
                ],
            },
            {
                'name': 'Richmond', 
                'schedules': [
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    }
                ],
            },
            {
                'name': 'Richmond', 
                'schedules': [
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    }
                ],
            },
            {
                'name': 'Richmond', 
                'schedules': [
                    {
                        'destination': 'Warm Springs', 
                        'minutes': '16', 
                        'arrival_time': '10:15 pm',
                    }
                ],
            },
        ],
    }

    return render(request, 'pages/base_etas.html', context)


