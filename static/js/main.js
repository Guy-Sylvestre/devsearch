

//GET SEARCH FORM AND LINKS
let searchForm = document.getElementById("searchForm");
let pagelinks = document.getElementsByClassName("page-link");


//ENSURE SEARCH FORM EXISTS 
if (searchForm) {
    for (let i = 0; pagelinks.length > i; i++){
        pagelinks[i].addEventListener("click", function (e) {
            e.preventDefault();

            //GET THE DATA ATTRIBUTE
            let page =this.dataset.page

            //ADD HIDDEN SEARCH INPUT TO FORM
            searchForm.innerHTML += `<input value="${page}" name="page" hidden/>`;

            //SUBMIT FORM
            searchForm.submit();
        })
    }
}
