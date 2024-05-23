describe("Take Code", () => {
    const EMAIL = "Dinara";
    const PASSWORD = "Dinara06!";
    
    const BASEURL = Cypress.config().baseUrl;
    const URLMAIN = BASEURL + "/";
    const URLLOGIN = BASEURL + "/login/index.php";

    it("Checking take code: server didn't answer", () => {
      cy.visit(URLLOGIN);
      cy.login(EMAIL, PASSWORD);
      cy.visit(BASEURL + "/proctor_ecg/proctor_ecg_init/");
      cy.get("div > input[id=id_submitbutton]").click();
      cy.get("section[id=region-main] > div ").contains(
        "Сервер недоступен. Зайдите позже("
      );
    });
  
  it("Checking take code: get code", () => {
    cy.visit(URLLOGIN);
    cy.login(EMAIL, PASSWORD);
    cy.visit(BASEURL + "/proctor_ecg/proctor_ecg_init/");
    cy.get("div > input[id=id_submitbutton]").click();
    cy.get("section[id=region-main] > div ").contains(
      "gen_code"
    );
  });
        
  it("Checking take code: incorrect data in input", () => {
    cy.visit(URLLOGIN);
    cy.login(EMAIL, PASSWORD);
    cy.visit(BASEURL + "/proctor_ecg/proctor_ecg_init/");
    cy.get("input[id=id_course_name]").click().type("JNIHIU");
    cy.get("input[id=id_quiz_name]").click().type("KHGUYUYIT");
    cy.get("div > input[id=id_submitbutton]").click();
    cy.get("section[id=region-main] > div ").contains(
      "Can't find data record in database table course."
    );
  });

  it("Checking take code: NO permission to take the code", () => {
    cy.visit(BASEURL + "/proctor_ecg/proctor_ecg_init/");
    cy.get("div > input[id=id_submitbutton]").should("not.exist");
  });
});
