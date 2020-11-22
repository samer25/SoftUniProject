// document.querySelector(".read_more").onclick = changeClass

function changeClass(id) {
    const content = document.querySelector(".extra_content-" + id)
    const less = document.querySelector(".less-" + id);
    const btn = document.querySelector(".read_more-" + id);
    if (content.style.display === "block") {
        content.style.display = "none";
        less.style.display = 'block';
        btn.innerHTML = '<i class="fi-arrow-down"></i> ';
    } else {


        content.style.display = "block";
        content.style.backgroundColor = "#ffffff";
        less.style.display = 'none';
        btn.innerHTML = '<i class="fi-arrow-up"></i> ';
    }

}

