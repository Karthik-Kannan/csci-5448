var testr = angular.module('testr', []);

testr.controller('questionController',function ($scope,$http)
{
    $scope.userOptions = [{text:'Single Choice', id:0}, {text:'Multi Choice', id:1}, {text:'Boolean',id:2},  {text:'Text', id:3},{text:'Code', id:3}];;

    $scope.createQuestion = function()
    {
        console.log("Question:" + $scope.Question);
        console.log("Category:" + $scope.Category);
        console.log("Max Marks:" + $scope.MaxMarks);
        console.log("Answer Type:" + $scope.answerType.selected);
        console.log("Reference Answer:" + $scope.referenceAnswer);
    }

});