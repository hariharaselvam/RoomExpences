/**
 * Created by hariharaselvam on 11/12/16.
 */
window[appName].controller('editable_controller', function ($rootScope, $scope, $state, http ) {

    $rootScope.title = "Expenses";

    http.Requests("get","/api/expense/editable/","").success(function (response) {

        $scope.expenses = response;
        for(i=0;i<$scope.expenses.length;i++)
        {
            $scope.expenses[i]['edit']="edit";
            $scope.expenses[i]['index']=i;
        }

    });

    $scope.editable = function (i) {
        if($scope.expenses[i]['edit']=="edit")
        {
            $scope.expenses[i]['edit']="ok"
        }
        else
        {
            var url = "/api/expense/editable/"+$scope.expenses[i]['id']+"/";
            var param = {"amount":$scope.expenses[i]['amount']}
            http.Requests("post",url,param).success(function (response) {
                 $scope.response = response.result;
            })
            $scope.expenses[i]['edit']="edit"
        }
    }


});