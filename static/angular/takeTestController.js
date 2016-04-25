var testr = angular.module('testr',['ngRoute']);


testr.controller('takeTestController',['$scope','$http',function ($scope,$http)
{

        $scope.answers = {};

        $scope.handleCheckEvent = function(parentDiv) {
        //console.log("click");
        var selectedCheckboxes = $('#' + parentDiv).find("input[type=checkbox]:checked").siblings("span");
        console.log(selectedCheckboxes);
            $scope.answers[parentDiv] = [];
        selectedCheckboxes.map(function(){
            $scope.answers[parentDiv].push($(this).html());
        });

        };

        $scope.getContent = function()
        {
            console.log($scope.answers)

            //data =
            //{
            //    testName: $scope.testName,
            //    questions: $scope.ids,
            //    startTime: $scope.startTime,
            //    durationOfTest: $scope.dOfTest,
            //    expiryDate: $scope.expTime,
            //    category: $scope.category,
            //    course: $scope.course
            //}
            //
            //var config =
            //{
            //    headers :
            //    {
            //        'Content-Type': 'application/json'
            //    }
            //}
            //
            //console.log(data)
            //
            //$http.post('setTest', data, config)
            //    .success(function (data, status, headers, config) {
            //        $scope.PostDataResponse = data;
            //        console.log("test");
            //        //$scope.changeView('index')
            //        //window.location.href = 'index';
            //        //$location.path('/index');
            //
            //    })
            //    .error(function (data, status, header, config) {
            //        $scope.ResponseDetails = "Data: " + data +
            //            "<hr />status: " + status +
            //            "<hr />headers: " + header +
            //            "<hr />config: " + config;
            //    });


        }



    
}]);

