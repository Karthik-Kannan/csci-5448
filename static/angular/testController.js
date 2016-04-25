var testr = angular.module('testr',['ngRoute']);


//
//testr.controller('indexController',function ($scope,$http) {
//
//});

testr.controller('testController',['$scope','$http','$route', '$routeParams','$location',function ($scope,$http,$route, $routeParams,$location)
{


    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;

    console.log("Route: " ,$scope.$route , " ", "Location: ",$scope.$location, " " , "Route Params: ", $scope.$routeParams )
    $scope.userOptions = [{text:'Single Choice', id:0}, {text:'Multi Choice', id:1}, {text:'Boolean',id:2},  {text:'Text', id:3},{text:'Code', id:4}];;

    $scope.changeView = function(view)
    {
        $location.path(view); // path not hash
    }
    
    $scope.handleCheckEvent = function() {
        //console.log("click");
        var selectedCheckboxes = $("input[type=checkbox]:checked").parent().parent().find("p");
        $scope.ids = [];
        selectedCheckboxes.map(function(){
            $scope.ids.push($(this).html());
        });
        //console.log($scope.ids);
    };
    
     $scope.getContent = function()
    {
        data = 
        {
            testName: $scope.testName,
            questions: $scope.ids,
            startTime: $scope.startTime,
            durationOfTest: $scope.dOfTest,
            expiryDate: $scope.expTime,
            category: $scope.category,
            course: $scope.course
        }
        
        var config =
        {
            headers :
            {
                'Content-Type': 'application/json'
            }
        }
        
        console.log(data)
        
        $http.post('setTest', data, config)
            .success(function (data, status, headers, config) {
                $scope.PostDataResponse = data;
                console.log("test");
                //$scope.changeView('index')
                window.location.href = 'teacher';
                //$location.path('/index');

            })
            .error(function (data, status, header, config) {
                $scope.ResponseDetails = "Data: " + data +
                    "<hr />status: " + status +
                    "<hr />headers: " + header +
                    "<hr />config: " + config;
            });
        

    }
    
}]);

