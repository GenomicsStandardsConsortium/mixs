name: New Term Request
description: "For us to assess a new term request we require the following details:"
title: "New term proposal: "
labels: [NewTerm]
body:
  - type: checkboxes
    attributes:
      label: Checklist
      description: >
        Please make sure you check all these items before submitting your feature request.
      options:
        - label: I have reviewed the existing MIxS checklists and extensions that the term does not exist.
          required: true
  - type: input
    attributes:
      label: Name
      description: >
        The name of the term. Previously known as 'Term name'
    validations:
      required: true
  - type: input
    attributes:
      label: Title
      description: >
        A version of the name with less than 20 characters and no spaces. Previously known as 'Structured comment name'.
    validations:
      required: true
  - type: textarea
    attributes:
      label: Description
      description: >
        A clear and concise description of the term. Previously known as 'Definition'.
    validations:
      required: true
  - type: input
    attributes:
      label: Short description of pattern or range.
      description: >
        The expected type of information the term will hold. Previously known as 'Expected value'.
      placeholder: >
        "e.g., text or EFO and/or OBI etc...".
    validations:
      required: true
  - type: input
    attributes:
      label: Pattern or range syntax
      description: >
        The pattern of the value that the term will be checked against. Previously known as 'Value syntax'.
      placeholder: >
        "e.g. {float} {unit}|{termLabel} {[termID]}|{text}|{timestamp} etc...".
    validations:
      required: true
  - type: input
    attributes:
      label: Example
      description: >
        An example value for the term/slot. The example value must follow the pattern/syntax described above.
    validations:
      required: true
  - type: input
    attributes:
      label: Unit
      description: >
        The preferred unit if appropriate. Previously known as 'Preferred unit'.
      placeholder: >
        "e.g, millliter, gram, milligram, liter".
    validations:
      required: false
  - type: input
    attributes:
      label: Requirement
      description: >
        Should the term/slot be considered 'Required' or 'Recommended', and if so, for which checklist/extension.
  - type: dropdown
    attributes:
      label: Multivalued
      description: >
        Could the term be used multiple times in a checklist/package to provide additional meta information.
      options:
        - "Yes"
        - "No"
  - type: input
    attributes:
      label: Extensions(s)
      description: >
        List any extensions that should include the new term
    validations:
      required: false
