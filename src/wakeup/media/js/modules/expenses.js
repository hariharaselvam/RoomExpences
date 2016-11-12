/**
 * Created by hariharaselvam on 11/12/16.
 */
window[appName].controller('expenses_controller', function ($rootScope, $scope, $state, http ) {

    $rootScope.title = "Expenses";

    http.Requests("get","/api/expense/expense/","").success(function (response) {

            $scope.expenses = response;

    });


});
