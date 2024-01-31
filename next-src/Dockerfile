FROM node:18-alpine AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /next-src

COPY package.json ./
RUN yarn

FROM node:18-alpine AS builder
WORKDIR /next-src
COPY --from=deps /next-src/node_modules ./node_modules
COPY . .

ENV NEXT_TELEMETRY_DISABLED 1

RUN yarn build

FROM node:18-alpine AS runner
WORKDIR /next-src

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder --chown=nextjs:nodejs /next-src/.next ./.next
COPY --from=builder /next-src/node_modules ./node_modules
COPY --from=builder /next-src/package.json ./package.json

USER nextjs

EXPOSE 3000

ENV PORT 3000

CMD ["yarn", "start"]
