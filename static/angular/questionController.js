var testr = angular.module('testr',['ngRoute']);


//
//testr.controller('indexController',function ($scope,$http) {
//
//});

testr.controller('questionController',['$scope','$http','$route', '$routeParams','$location',function ($scope,$http,$route, $routeParams,$location)
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

    $scope.createQuestion = function()
    {
        console.log("Question:" + $scope.question);
        console.log("Category:" + $scope.category);
        console.log("Max Marks:" + $scope.maxMarks);
        console.log("Answer Type:" + $scope.answerType.selected);
        console.log("Reference Answer:" + $scope.referenceAnswer);


        var data = $.param({
                question: $scope.Question,
                category: $scope.Category,
                maxMarks: $scope.maxMarks,
                answerType: $scope.answerType.selected,
                referenceAnswer: $scope.referenceAnswer,
                options: $scope.options
            });

        console.log(data)
        var config =
        {
            headers :
            {
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
            }
        }

        $http.post('setQuestion', data, config)
            .success(function (data, status, headers, config) {
                $scope.PostDataResponse = data;
                console.log("test");
                //$scope.changeView('index')
                window.location.href = 'index';
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

//
//testr.config(function($routeProvider){
// $routeProvider.when('/index', {
//        controller: indexController,
//        templateUrl: 'index'
//    })
//});
//
//function indexController()
//{
//
//}