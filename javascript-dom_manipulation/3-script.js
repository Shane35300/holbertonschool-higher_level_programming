let header = document.querySelector("header");
header.addEventListener("click", () => {
	if (header.classList.contains("green")) {
		header.classList.add("red");
		header.classList.remove("green");
	} else {
		header.classList.add("green");
		header.classList.remove("red");
	}
})
