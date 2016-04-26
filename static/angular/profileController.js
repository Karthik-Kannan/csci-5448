var testr = angular.module('testr',[]);

testr.controller('profileController',['$scope',function ($scope)
{
    var page = 'student';
    $scope.handleCheckEvent = function()
    {
        page = 'teacher';
    }

    $scope.handleReCheckEvent = function()
    {
        page = 'student';
    }

    $scope.changePage = function()
    {
        window.location.href = page;
    }

}]);

