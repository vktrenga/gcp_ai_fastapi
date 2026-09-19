import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from services.tenant.db.database import Base
import bcrypt

class Tenant(Base):
    __tablename__ = "tenant"
    tenant_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_name = Column(String, nullable=False)
    domain_name = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email_id = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def set_password(self, raw_password: str):
        self.password = bcrypt.hashpw(
            raw_password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, raw_password: str) -> bool:
        return bcrypt.checkpw(
            raw_password.encode("utf-8"), self.password.encode("utf-8")
        )
