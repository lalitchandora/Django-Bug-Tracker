function openprojectform(){
    window.location = 'createproject/';
}

function openbugform(project_id){
    window.location = 'http://localhost:8000/bug/addbug/'+project_id;
}
