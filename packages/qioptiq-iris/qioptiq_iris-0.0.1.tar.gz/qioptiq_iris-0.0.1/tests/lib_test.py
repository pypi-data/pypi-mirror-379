import qioptiq_iris as qi
import pytest

class TestCommandFrame:
    def test_repr(self):
        address = 1
        
        # enable
        cmd = qi.Command.ENABLE
        f = qi.CommandFrame(address, cmd, 1)
        assert str(f) == f"#{address:02}020001\r\n"
        
        # disable
        cmd = qi.Command.ENABLE
        f = qi.CommandFrame(address, cmd, 0)
        assert str(f) == f"#{address:02}020000\r\n"
        
        # set laser power
        cmd = qi.Command.SET_POWER
        f = qi.CommandFrame(address, cmd, 182)
        assert str(f) == f"#{address:02}030182\r\n"
                
        # query laser power
        cmd = qi.Command.POWER
        f = qi.CommandFrame(address, cmd)
        assert str(f) == f"#{address:02}440000\r\n"
        
        # set laser address
        cmd = qi.Command.SET_ADDRESS
        f = qi.CommandFrame(address, cmd, 78)
        assert str(f) == f"#{address:02}120078\r\n"
        
    def test_address_space(self):
        with pytest.raises(ValueError):
            qi.CommandFrame(0, qi.Command.POWER)
        with pytest.raises(ValueError):
            qi.CommandFrame(100, qi.Command.POWER)
        
    def test_parse_str(self):
        address = 1
        
        # enable
        input = f"#{address:02}020001\r\n"
        f = qi.CommandFrame.parse_str(input)
        assert f.address == address
        assert f.command == qi.Command.ENABLE
        assert f.data == 1
        
        # disable
        input = f"#{address:02}020000\r\n"
        f = qi.CommandFrame.parse_str(input)
        assert f.address == address
        assert f.command == qi.Command.ENABLE
        assert f.data == 0
        
        # set laser power
        input = f"#{address:02}030182\r\n"
        f = qi.CommandFrame.parse_str(input)
        assert f.address == address
        assert f.command == qi.Command.SET_POWER
        assert f.data == 182
                
        # query laser power
        input = f"#{address:02}440000\r\n"
        f = qi.CommandFrame.parse_str(input)
        assert f.address == address
        assert f.command == qi.Command.POWER
        assert f.data == 0
                
        # set laser address
        input = f"#{address:02}120078\r\n"
        f = qi.CommandFrame.parse_str(input)
        assert f.address == address
        assert f.command == qi.Command.SET_ADDRESS
        assert f.data == 78
                
    def test_parse_str_invalid(self):
        with pytest.raises(ValueError):
            qi.CommandFrame.parse_str("xxccdddd\r\n")
        with pytest.raises(ValueError):
            qi.CommandFrame.parse_str("#xxccdddd")
        with pytest.raises(ValueError):
            qi.CommandFrame.parse_str("#xxcc\r\n")
        with pytest.raises(ValueError):
            qi.CommandFrame.parse_str("#xx00dddd\r\n")