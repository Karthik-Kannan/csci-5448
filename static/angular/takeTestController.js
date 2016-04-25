var testr = angular.module('testr',['ngRoute']);


testr.controller('takeTestController',['$scope','$http',function ($scope,$http)
{

        $scope.answers = {};

        $scope.overallContent = ""
        $scope.getOverallData = function(content)
        {
            console.log(content)
            $scope.overallContent = content;
        }

        $scope.handleCheckEvent = function(parentDiv,type) {
            //console.log("click");
            console.log(type)
            if (type == 1) {
                var selectedCheckboxes = $('#' + parentDiv).find("input[type=checkbox]:checked").siblings("span");
                console.log(selectedCheckboxes);
                $scope.answers[parentDiv] = [];
                selectedCheckboxes.map(function () {
                    $scope.answers[parentDiv].push($(this).html());
                });


            }
            else if (type == 0 || type == 2 ) {
                var selectedCheckboxes = $('#' + parentDiv).find("input[type=radio]:checked").siblings("span");
                console.log(selectedCheckboxes);
                $scope.answers[parentDiv] = [];
                selectedCheckboxes.map(function () {
                    $scope.answers[parentDiv].push($(this).html());
                });

            }
            else if (type == 3 ) {
                $scope.answers[parentDiv] = $('#' + parentDiv).find("input[type=text]").val()
            };
        };

        $scope.getContent = function()
        {
            answers = $scope.answers
            test = $scope.overallContent
            data = { 'testName': test, 'answers': answers }
            console.log(data)

            var config =
            {
                headers :
                {
                    'Content-Type': 'application/json'
                }
            }

            //console.log(data)
            //
            $http.post('setTest', data, config)
                .success(function (data, status, headers, config) {
                    $scope.PostDataResponse = data;
                    console.log("test");
                    //$scope.changeView('index')
                    //window.location.href = 'index';
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

