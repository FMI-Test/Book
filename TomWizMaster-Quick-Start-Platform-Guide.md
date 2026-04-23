# TomWizMaster Quick Start Platform Guide

Date: April 20, 2026
Status: Draft to port into TomWizMaster

## What This Is

This is not a cloud-vendor manifesto.

It is a practical quick-start guide for TomWizMaster as a human-intelligence plus AI repo that may need deployment, auth, storage, and tooling choices without turning into a pure cloud-strategy repository.

TomWizMaster is about ideas, workflows, synthesis, and systems thinking first.
Infrastructure is a support layer, not the product identity.

## Index

1. Design Principle
2. Deployment Modes
3. Stack Options
4. Recommended Default
5. How To Choose a Stack
6. Third-Party Tool Guidelines
7. Domain and Site Setup Checklist
8. What Not To Overbuild

## 1. Design Principle

Use the smallest stack that preserves:

1. clarity
2. speed
3. security
4. maintainability
5. future migration room

This is primarily a Dev, R&D, publishing, and workflow repo.

That means the default should optimize for:

- fast iteration
- low ops burden
- good auth and content separation
- strong documentation

It should not optimize prematurely for mission-critical multi-region enterprise complexity unless the actual product surface demands it.

## 2. Deployment Modes

### Mode A: Local / Dev / R&D

Use when experimenting, writing, prototyping, or validating workflows.

Characteristics:

- fast setup
- low cost
- low ceremony
- local scripts and container-friendly tooling

### Mode B: Public Web / Content Delivery

Use when publishing public-safe docs, essays, guides, and lightweight app surfaces.

Characteristics:

- CDN/static hosting
- simple app/API layer
- clear analytics and auth boundary

### Mode C: Restricted Member Surface

Use when signed-in content, role-based access, or gated experiences become necessary.

Characteristics:

- real auth
- content zoning
- audit trail
- secure media access

### Mode D: Enterprise / Partner / Hybrid

Use only when external orgs, private integrations, or compliance-heavy workloads actually appear.

Characteristics:

- federation
- stronger IAM controls
- more structured IaC
- environment separation

## 3. Stack Options

### Option 1: AWS

Best for:

- fast startup path
- content + API + restricted media
- good path from prototype to real production

Typical shape:

- S3 + CloudFront
- Lambda / API Gateway or ECS/Fargate
- RDS/Aurora PostgreSQL
- Cognito

### Option 2: Azure

Best for:

- enterprise identity
- Microsoft-heavy audience
- stronger default fit for Entra-based orgs

Typical shape:

- Static Web Apps / App Service
- Functions / Container Apps
- Azure Database for PostgreSQL
- Entra External ID

### Option 3: GCP

Best for:

- teams already comfortable with Google identity, analytics, or ML tooling
- app teams that want a cleaner platform experience than raw AWS in some areas

Typical shape:

- Cloud Run
- Cloud Storage
- Cloud SQL PostgreSQL
- Identity via Google or external IdP

### Option 4: Oracle Cloud

Best for:

- cost-sensitive experiments where OCI advantages are already known
- niche org requirements

Default stance:

- not the default recommendation here
- use only with a clear reason

### Option 5: Container-first portable stack

Best for:

- teams wanting runtime portability
- mixed environments
- eventual private/hybrid deployments

Typical shape:

- Docker Compose for dev
- Kubernetes only when there is a real operational need

### Option 6: Private / Hybrid / Multi-cloud

Best for:

- regulated workloads
- partner-specific hosting constraints
- real cross-cloud dependency reasons

Default stance:

- avoid as a starting point
- adopt only after concrete workload pressure

## 4. Recommended Default

For TomWizMaster, recommend one hero path:

### Default Recommendation: AWS-first, container-aware, cloud-neutral in design

Why:

1. Lowest friction path from docs/prototype to real service.
2. Strong content hosting and signed media patterns.
3. Good enough identity path for restricted membership.
4. Easy to keep the architecture small while leaving room to grow.
5. Avoids premature hybrid or multi-cloud complexity.

Practical rule:

- design portable
- deploy simple
- keep one hero cloud until reality forces otherwise

## 5. How To Choose a Stack

Pick based on real constraints, not brand identity.

### Choose AWS if

- you want the simplest all-around starting point
- content, auth, and restricted media matter
- the team is comfortable with pragmatic ops

### Choose Azure if

- identity and enterprise federation are the main problem
- Microsoft ecosystem alignment matters more than raw simplicity

### Choose GCP if

- developer ergonomics and Google-native workflows dominate
- ML/data service fit is the real reason

### Choose container-first if

- local reproducibility matters immediately
- runtime portability matters more than platform convenience

### Choose hybrid or multi-cloud only if

- customers, partners, or regulation require it
- not because it sounds sophisticated

## 6. Third-Party Tool Guidelines

Use third-party tools only when they remove real burden.

Preferred categories:

1. Auth provider
2. Email/notification provider
3. Observability/logging
4. CDN/WAF
5. Object storage / media optimization

Selection rules:

1. Prefer standard protocols: OIDC, OAuth 2.0, SAML, SCIM, SMTP, webhooks.
2. Prefer tools with export paths and low lock-in.
3. Avoid overlapping vendors that solve the same problem poorly.
4. Keep the canonical source of truth in repo docs and config, not in vendor dashboards alone.
5. If a third-party tool becomes core to the product path, document why it was chosen and what would replace it if needed.

## 7. Domain and Site Setup Checklist

For `tomwiz.io` or a sibling site surface:

### Domain baseline

1. Register or confirm domain ownership.
2. Put DNS under a reliable provider.
3. Define subdomain plan early.

Suggested baseline:

- `tomwiz.io` - primary web
- `www.tomwiz.io` - canonical redirect target or alias
- `app.tomwiz.io` - signed-in application surface
- `docs.tomwiz.io` - documentation if split later
- `media.tomwiz.io` - optional media delivery boundary
- `auth.tomwiz.io` - optional auth domain if architecture needs it

### Core setup

1. DNS records
2. TLS certificates
3. CDN/WAF
4. canonical redirects
5. monitoring/uptime
6. SPF/DKIM/DMARC for mail if outbound email exists

### Access setup

1. public routes
2. signed-in routes
3. restricted member routes
4. admin/editor routes
5. consent and policy pages

### Environment setup

1. dev
2. preview/staging
3. prod

### Operational setup

1. secrets management
2. backup policy
3. basic incident path
4. audit logging
5. analytics with privacy boundary

## 8. What Not To Overbuild

Do not start with:

- full multi-cloud active-active
- Kubernetes without a real scaling or isolation need
- too many social login providers
- separate microservices for everything
- enterprise-grade policy machinery before the product surface exists

Start with:

- one hero cloud
- one database
- one auth layer
- one media storage path
- one deploy path
- one clear public vs restricted boundary

## Bottom Line

TomWizMaster should teach how to think and choose, not pretend every repo is a cloud platform strategy deck.

The recommended stance is simple:

- AWS first
- portable design
- restricted content behind real auth
- multi-cloud only when reality forces it
- infrastructure serves the work; it does not become the work
