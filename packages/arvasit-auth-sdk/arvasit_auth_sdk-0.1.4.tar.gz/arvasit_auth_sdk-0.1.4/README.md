# Arvasit Authentication SDK

A comprehensive authentication SDK for Node.js and Python with TypeScript/Pydantic support.

## 🚀 Quick Start

### Node.js
```bash
npm install @pratik_25/auth-sdk
```

```typescript
import { AuthService, AuthServiceConfig } from '@pratik_25/auth-sdk';

const config: AuthServiceConfig = {
  url: 'https://your-auth-service.com',
  publicKey: 'your_public_key',
  secretKey: 'your_secret_key'
};

const authService = new AuthService(config);
```

### Python
```bash
pip install arvasit-auth-sdk
```

```python
from auth_sdk import AuthService, AuthServiceConfig

config = AuthServiceConfig(
    url="https://your-auth-service.com",
    public_key="your_public_key",
    secret_key="your_secret_key"
)

auth_service = AuthService(config)
```

## 📋 Available Methods

### User Management
- `registerUser(data)` - Register new user
- `loginUser(data)` - User login
- `logoutUser(token)` - User logout
- `refreshToken(token)` - Refresh access token
- `verifyToken(token)` - Verify token validity

### Password Management
- `forgotPassword(email)` - Send password reset
- `resetPassword(data)` - Reset password
- `changePassword(data)` - Change password
- `verifyPasswordReset(data)` - Verify reset token

### Two-Factor Authentication
- `enable2FA(userId)` - Enable 2FA
- `disable2FA(userId)` - Disable 2FA
- `verify2FA(data)` - Verify 2FA code
- `generate2FABackupCodes(userId)` - Generate backup codes

### User Profile
- `getUserProfile(userId)` - Get user profile
- `updateUserProfile(userId, data)` - Update profile
- `deleteUser(userId)` - Delete user account

### Session Management
- `getActiveSessions(userId)` - Get active sessions
- `revokeSession(sessionId)` - Revoke session
- `revokeAllSessions(userId)` - Revoke all sessions

### Verification
- `sendEmailVerification(email)` - Send email verification
- `verifyEmail(data)` - Verify email
- `sendPhoneVerification(phone)` - Send phone verification
- `verifyPhone(data)` - Verify phone

## 🔧 Configuration

Both SDKs support the same configuration:

```typescript
interface AuthServiceConfig {
  url: string;           // Your auth service URL
  publicKey: string;     // Public API key
  secretKey: string;    // Secret API key
}
```

## 📚 Examples

See the `examples/` directory for detailed usage examples.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.