class UserActions():
    """Collection of methods to handle user-based library calls to mixin with other classes. Child classes must have self.client."""

    async def _user_action_follow(self, handle: str, following: str, followers_count: int | None = None) -> dict:
        """Action to follow/unfollow user"""

        if handle == self.client.handle:
            self.app.notify(f'Unable to follow self', severity="warning")
            success = False

        elif following is None:
            result = await self.client.follow(handle)
            if result:
                self.app.notify(f'Followed @{handle}')
                following = result
                if followers_count:
                    followers_count += 1
                success = True
            else:
                self.app.notify(f'Failed to follow @{handle}', severity="error")
                success = False

        else:
            result = await self.client.remove_follow_record(following)
            if result:
                self.app.notify(f'Unfollowed @{handle}')
                following = None
                if followers_count:
                    followers_count -= 1
                success = True
            else:
                self.app.notify(f'Failed to unfollow @{handle}', severity="error")
                success = False

        return {
            'success': success,
            'following': following,
            'followers_count': followers_count,
        }


    async def _user_action_mute(self, handle: str, muted: bool) -> bool:
        """Action to mute/unmute user"""

        if handle == self.client.handle:
            self.app.notify(f'Unable to mute self', severity="warning")
            success = False

        elif not muted:
            result = await self.client.mute_user(handle)
            if result:
                self.app.notify(f'Muted @{handle}')
                muted = True
                success = True

            else:
                self.app.notify(f'Failed to mute @{handle}', severity="error")
                success = False

        else:
            result = await self.client.unmute_user(handle)
            if result:
                self.app.notify(f'Unmuted @{handle}')
                muted = False
                success = True
            else:
                self.app.notify(f'Failed to unmute @{handle}', severity="error")
                success = False

        return {
            'success': success,
            'muted': muted,
        }

    async def _user_action_block(self, handle: str, blocking: str, following: str, followers_count: int | None = None) -> bool:
        """Action to block/unblock user"""

        if handle == self.client.handle:
            self.app.notify(f'Unable to block self', severity="warning")
            success = False

        elif blocking is None:
            result = await self.client.block_user(handle)
            if result:
                blocking = result

                # unfollow if following
                if following is not None:
                    unfollow_result = await self.client.remove_follow_record(following)
                    if unfollow_result:
                        self.app.notify(f'Blocked and unfollowed @{handle}')
                        following = None
                        if followers_count:
                            followers_count -= 1

                else:
                    self.app.notify(f'Blocked @{handle}')

                success = True

            else:
                self.app.notify(f'Failed to block @{handle}', severity="error")
                success = False


        else:
            result = await self.client.delete_block(blocking)
            if result:
                self.app.notify(f'Unblocked @{handle}')
                blocking = None
                success = True
            else:
                self.app.notify(f'Failed to unblock @{handle}', severity="error")
                success = False

        return {
            'success': success,
            'blocking': blocking,
            'following': following,
            'followers_count': followers_count,
        }
