# TomWiz Restricted Access Architecture

Date: April 20, 2026
Status: Draft for implementation planning

## Index

1. Problem Statement
2. Content Zoning Model
3. Public Repo Sanitization Rules
4. Restricted Membership Model
5. Identity and Access Architecture
6. Deployment Options
7. Recommended Path
8. Rollout Plan

## 1. Problem Statement

There are really two different publishing problems here:

1. Keep the public GitHub repo safe, collaboration-friendly, and broadly PG-13.
2. Preserve a path for invite-only or signed-in access to restricted material on a separate web surface such as `tomwiz.io`.

Those two goals should not be solved in the same place.

GitHub should remain the canonical public source repo.
Restricted content should move to an application layer with real access control, auditability, and policy separation.

## 2. Content Zoning Model

Use four zones.

### Zone A: Public

- GitHub-safe
- broadly PG-13
- docs, code, public essays, non-explicit visuals, metadata, prompts that do not require adult gating

### Zone B: Sensitive but Public-Safe

- analytical discussion of sex, trauma, violence, and other charged topics
- no explicit imagery
- abstraction, composition, policy, redaction, or scholarly framing only

### Zone C: Restricted Member Content

- maturity-restricted essays or visual material that should not live in a public repo
- requires account, terms acceptance, age gate, and explicit policy boundary

### Zone D: Private Internal Intake

- raw assets
- moderation queues
- source material under review
- unverified or explicit references
- never mirrored to the public repo

## 3. Public Repo Sanitization Rules

Public GitHub content should be sanitized at the source-of-truth layer.

Rules:

1. Replace explicit media with metadata, quarantine references, or analytical abstraction.
2. Keep filenames, tags, and references clean enough for public collaboration.
3. Move raw explicit assets to restricted or private storage.
4. Keep public chapter text analytical rather than graphic.
5. Treat GitHub as documentation and publishing control, not as the adult-content delivery channel.

Operationally:

- public repo = Zone A + selective Zone B
- restricted site = Zone C
- internal archive = Zone D

## 4. Restricted Membership Model

If `tomwiz.io` becomes the controlled publication surface, the restricted area should support:

1. invite-only access for early/private review
2. standard self-service accounts for approved public members
3. age-gated or policy-gated content sections
4. role-based access such as `public`, `member`, `editor`, `moderator`, `admin`
5. audit logs for sign-in, consent, and content access events

Recommended capability set:

- email/password login
- Google sign-in
- Apple sign-in
- optional Facebook and X only if they are genuinely needed
- MFA support
- TOTP authenticator support
- enterprise federation for Microsoft Entra ID and Google Workspace where needed

## 5. Identity and Access Architecture

### Requirements

The identity layer should support:

- OIDC / OAuth 2.0 social login
- SAML or OIDC enterprise federation
- MFA and recovery flows
- RBAC at application level
- policy-aware session handling
- separation between authentication and authorization

### Recommended IAM shape

1. Identity Provider (IdP): central authentication service
2. Application RBAC: app-side roles and content entitlements
3. Content policy engine: determines whether a user can view Zone C content
4. Audit trail: login, consent, MFA enrollment, role changes, restricted-content access

### Practical provider options

#### Option A: AWS-first

- Amazon Cognito for user pools and federation
- social login through Google, Apple, Facebook
- SAML/OIDC federation for Microsoft Entra ID and Google Workspace
- app roles managed in the application database or JWT claims

Strengths:

- good AWS integration
- manageable cost early
- solid for serverless/web app patterns

Weaknesses:

- developer experience is acceptable, not elegant
- advanced identity customization can become awkward

#### Option B: Azure-first

- Microsoft Entra External ID / B2C style architecture
- native strength for enterprise identity and Microsoft ecosystem
- social identity support plus strong conditional access patterns

Strengths:

- excellent enterprise federation
- strong policy and compliance posture
- better fit if the long-term audience includes institutional or corporate users

Weaknesses:

- can feel heavy for a smaller product
- pricing and product complexity need active control

#### Option C: Neutral identity layer

- Auth0, Keycloak, or similar centralized identity platform
- app hosted wherever is best
- identity decoupled from cloud choice

Strengths:

- fastest path to many login methods
- least coupling to one cloud

Weaknesses:

- another vendor or service to manage
- self-hosted Keycloak adds operational overhead

## 6. Deployment Options

### Option 1: AWS Hero, multi-cloud aware

Use AWS as the primary runtime.

Suggested stack:

- Frontend: S3 + CloudFront or Next.js on Amplify / ECS
- API: API Gateway + Lambda or ECS/Fargate
- Database: Aurora PostgreSQL or RDS PostgreSQL
- Identity: Cognito
- Private media: S3 with signed URLs
- WAF and bot protection: AWS WAF + Shield basics
- Observability: CloudWatch + centralized app logs

Use GCP or Azure only when a service is truly better or already required.

Best for:

- content-heavy site
- cost-aware startup posture
- serverless-first or lightweight app team

### Option 2: Azure Hero, enterprise-heavy

Suggested stack:

- Frontend: Static Web Apps or App Service
- API: Azure Functions / App Service / Container Apps
- Database: Azure Database for PostgreSQL
- Identity: Entra External ID
- Restricted media: Blob Storage with signed access
- WAF/CDN: Front Door + WAF
- Monitoring: Application Insights + Log Analytics

Best for:

- enterprise-heavy audience
- strong Microsoft identity and compliance alignment
- deeper corporate federation needs

### Option 3: Mixed cloud with neutral edge

Suggested shape:

- frontend on Vercel/Cloudflare or AWS/Azure static layer
- neutral IdP
- app API on AWS or Azure
- object storage split by workload
- CDN/WAF in front

Best for:

- product experimentation
- lower lock-in
- teams comfortable with operational complexity

Weakness:

- easiest way to create accidental complexity too early

## 7. Recommended Path

Recommended default: AWS hero deployment, with a neutral architecture mindset.

Why:

1. The current repo and automation posture already fit lightweight, modular, scripting-friendly operations.
2. AWS gives the easiest early path to web app, storage, signed media access, and controlled private/public separation.
3. Cognito is good enough for the first real release if the app-side RBAC is designed cleanly.
4. If enterprise identity grows later, federation can be extended rather than forcing a full rewrite on day one.

Recommended identity stance:

- start with email/password, Google, and Apple
- add MFA from day one
- add Microsoft Entra ID and Google Workspace federation when there is a real institutional need
- add Facebook or X only if there is a genuine audience reason

If the product becomes identity-heavy, partner-heavy, or compliance-heavy, re-evaluate moving the identity layer to Entra External ID or a neutral IdP.

## 8. Rollout Plan

### Phase 1: Repo hygiene

1. Keep GitHub public and PG-13.
2. Sanitize filenames, references, and chapter text.
3. Maintain quarantine and restricted-content separation.

### Phase 2: Restricted site foundation

1. Launch `tomwiz.io` public shell.
2. Add auth and MFA.
3. Add member roles and restricted routes.
4. Move restricted assets out of repo into controlled object storage.

### Phase 3: Identity expansion

1. Add Google and Apple sign-in.
2. Add enterprise federation if required.
3. Add audit logging, consent records, and policy acceptance tracking.

### Phase 4: Multi-cloud or enterprise hardening

1. Add Azure or GCP only for real workload reasons.
2. Formalize IAM boundaries by environment.
3. Introduce infrastructure-as-code baseline and policy testing.

## Bottom Line

Do not solve adult-content gating inside the public GitHub repo.

Sanitize the repo.
Separate the content zones.
Put restricted material behind a real identity layer on `tomwiz.io`.
Start AWS-first unless enterprise identity pressure makes Azure-first the better choice.
