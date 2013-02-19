
function ExperienceListCtrl($scope, $http) {
    //this.experiences = Experience.query();

    $http.get('api/experiences/').success(function(data) {
        $scope.experiences = data.results;
    });

}
 
function ExperienceDetailCtrl($scope, $routeParams, Experience) {
 
    this.experience = Experience.get({experienceID:this.params.experienceID});
 
    this.saveExperience = function () {
        if (this.experience.id > 0)
            this.experience.$update({experienceID:this.experience.id});
        else
            this.experience.$save();
        window.location = "#/experiences";
    };
 
    this.deleteExperience = function () {
        this.experience.$delete({experienceID:this.experience.id}, function() {
            alert('Experience ' + experience.name + ' deleted');
            window.location = "#/experiences";
        });
    };
 
}