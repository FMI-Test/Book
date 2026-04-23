# TomWiz Domain Setup Checklist

Date: April 20, 2026
Status: Draft

## Core Domain

- [ ] Confirm registrar and domain ownership for `tomwiz.io`
- [ ] Set authoritative DNS provider
- [ ] Decide canonical root/`www` strategy
- [ ] Enable TLS for all public hostnames

## Suggested Subdomains

- [ ] `tomwiz.io`
- [ ] `www.tomwiz.io`
- [ ] `app.tomwiz.io`
- [ ] `docs.tomwiz.io`
- [ ] `media.tomwiz.io`
- [ ] `auth.tomwiz.io` if required

## Public vs Restricted Split

- [ ] Define public routes
- [ ] Define signed-in routes
- [ ] Define restricted-member routes
- [ ] Define admin/editor routes

## Security and Delivery

- [ ] CDN in front of public web
- [ ] WAF/basic bot protection
- [ ] signed media access for restricted content
- [ ] secrets management
- [ ] backup policy
- [ ] audit logging

## Identity

- [ ] email/password
- [ ] Google sign-in
- [ ] Apple sign-in
- [ ] MFA/TOTP
- [ ] enterprise federation only if needed

## Environments

- [ ] dev
- [ ] preview/staging
- [ ] prod

## Mail and Notifications

- [ ] SPF
- [ ] DKIM
- [ ] DMARC
- [ ] transactional email provider

## Repo Coordination

- [ ] keep GitHub repo public-safe
- [ ] keep restricted assets out of public repo
- [ ] document source-of-truth and publish-out model
