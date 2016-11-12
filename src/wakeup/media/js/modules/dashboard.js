/**
 * Created by hariharaselvam on 11/12/16.
 */
window[appName].controller('dashboard_controller', function ($rootScope, $scope, $state, http ) {

    $rootScope.title = "Dashboard";
    $scope.dashboard = {
        "page":"Dashboard"
    };

    $scope.add_amount = function () {
        var param = {"name":$scope.desc,"date":$scope.date,"amount":$scope.amount};
        http.Requests("post","/api/expense/expense/",param).success(function (response) {

            $scope.response = response.result;

        });
    }

});