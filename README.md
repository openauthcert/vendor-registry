[![Validate Vendor Registry](https://github.com/openauthcert/vendor-registry/actions/workflows/validate-vendors.yml/badge.svg)](https://github.com/openauthcert/vendor-registry/actions/workflows/validate-vendors.yml)
![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)

# 🗂️ OpenAuthCert Vendor Registry

This repository contains the **public registry of software projects and vendors** certified by the [Open Authentication Certification Initiative](https://openauthcert.org).

---

## 📜 Purpose

To maintain a public, open, machine-readable list of identity-integrated software solutions that meet the ethical access criteria of OpenAuthCert badges.

---

## 📂 Structure

```
.
├── vendors/
│   ├── acme-idp-project.json         # Example vendor entry
├── schema/
│   └── vendor-entry-schema.json     # Shared JSON Schema for validation
├── LICENSE                          # CC BY-SA 4.0
└── README.md
```

---

## 📄 Vendor Entry Format
Each vendor/project entry must:
- Be in a separate file under `vendors/`
- Follow the schema in `schema/vendor-entry-schema.json`
- Reference at least one valid badge from `badge-spec`

---

## ✅ Example Entry: `vendors/acme-idp-project.json`
```json
{
  "name": "Acme Identity Hub",
  "website": "https://acme.example.com",
  "repo": "https://github.com/acme/openidp",
  "badges": [
    {
      "id": "free-sso-idp",
      "version": "0.1",
      "certified_at": "2025-06-18",
      "certified_by": "OpenAuthCert Foundation"
    }
  ],
  "self_hosted": true,
  "notes": "Supports OIDC and LDAP in all editions; documentation and Docker image available."
}
```

---

## 📄 License
This repository is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

---

## 🤝 Contributing
To propose a new vendor or project, please:
- Fork this repository
- Add a `.json` file under `vendors/`
- Validate it using the schema in `schema/`
- Open a pull request

---

🔗 Return to project: https://openauthcert.org
